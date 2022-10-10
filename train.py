from ast import parse
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from utils import *
import argparse
import torch
import torch.nn as nn
from model import initilize_model
import torch.optim as optim
from ray import tune
from ray.tune.schedulers import ASHAScheduler


def parse_opt(known=False):

    parser = argparse.ArgumentParser()
    parser.add_argument('--batch_size', default=4, help='total batch size for all GPUs')
    parser.add_argument('--epochs', default=100, help='number of epochs')
    parser.add_argument('--adam', action='store_true', help='use torch.optim.Adam() optimizer')
    parser.add_argument('--sgd', action='store_true', help='use torch.optim.sgd() optimizer')
    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt
def train(model, optimizer, train_dataloader, val_dataloader = None, epochs =10):

   


    best_accuracy = 0
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Start training...\n")
    # for param in model.bert.parameters():
    #     param.requires_grad = False
    for epoch_i in range(1,10):
        
        total_loss = 0
        model.train()
        
        for step,batch in tqdm(enumerate(train_dataloader)):
            
            b_input_ids, b_attn_masks, b_labels = tuple(t.to(device) for t in batch)
            b_input_ids = b_input_ids.reshape((1,1,1002)).squeeze(0)
            b_attn_masks = b_attn_masks.reshape((1,1,1002)).squeeze(0)
            b_labels = b_labels.reshape((1,1,1)).squeeze(0)
            optimizer.zero_grad()
            
            logits = model( b_input_ids, b_attn_masks)
            
                     
            loss = loss_fn(logits,b_labels.float()) 
            
            total_loss += loss.item()
            
            loss.backward()
            
            optimizer.step()
               
        avg_train_loss = total_loss / len(train_dataloader)
        
    
        if test_dataloader is not None:
                
                val_loss, val_accuracy = evaluate(model, test_dataloader,opt)
                
                   
                if val_accuracy > best_accuracy:
                    best_accuracy = val_accuracy
                    torch.save({
                        'epoch': epoch_i + 1,
                        'model_state_dict': model.state_dict(),
                        'optimizer_state_dict': optimizer.state_dict(),
                        'loss': loss_fn,
                        }, 'best_mode_trained_after_37_epochs.pth')

                # scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'max',patience = 3)
                # scheduler.step(val_accuracy)
        print(f"Epoch: {epoch_i} | Training Loss: {avg_train_loss}  | Validation Loss: {val_loss}  | Accuracy: {val_accuracy:.2f}")
        with open('result.txt', 'a') as f:
            print(f"Epoch: {epoch_i} | Training Loss: {avg_train_loss}  | Validation Loss: {val_loss}  | Accuracy: {val_accuracy:.2f}", file=f) 
    print("\n")
    print(f"Training complete! Best accuracy: {best_accuracy:.2f}%.")
    


def evaluate(model,val_dataloader,opt):
    
    model.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    val_accuracy = []
    val_loss = []
    for batch in tqdm(val_dataloader):
        # Load batch to GPU
        b_input_ids, b_attn_masks, b_labels = tuple(t.to(device) for t in batch)
        b_input_ids = b_input_ids.reshape((1,1,1002)).squeeze(0)
        b_attn_masks = b_attn_masks.reshape((1,1,1002)).squeeze(0)
        b_labels = b_labels.reshape((1,4,1)).squeeze(0)
        with torch.no_grad():
                logits = model( b_input_ids, b_attn_masks)
        loss = loss_fn(logits, b_labels.float())

        val_loss.append(loss.item())
        preds = torch.round(torch.sigmoid(logits))
        
        accuracy = (preds.float() == b_labels.float()).cpu().numpy().mean() * 100

        val_accuracy.append(accuracy)
    
    val_loss = np.mean(val_loss)
    val_accuracy = np.mean(val_accuracy)

    return val_loss, val_accuracy 


if __name__ == "__main__":
    opt = parse_opt(True)
    model = initilize_model()
    opt = None
    data = pd.read_csv("final_data.csv")
    data = preprocessing(data)
    loss_fn = nn.BCEWithLogitsLoss()

    X_train, X_test, y_train, y_test = train_test_split_function(data)
    train_inputs,train_masks = preprocessing_for_bert(X_train[0:1000])
    test_inputs,test_masks = preprocessing_for_bert(X_test[0:1000])
    train_data = TensorDataset(train_inputs, train_masks,y_train[0:1000])
    train_sampler = RandomSampler(train_data)
    train_dataloader = DataLoader(train_data, sampler = train_sampler, batch_size = 1,drop_last=True)
    test_data = TensorDataset(test_inputs, test_masks,y_test[0:1000])
    test_sampler = RandomSampler(test_data)
    test_dataloader = DataLoader(test_data, sampler = test_sampler, batch_size = 1,drop_last=True)
    optimizer = optim.Adam(model.parameters(),lr=0.01,betas=(0.9,0.999),eps=1e-08,weight_decay=0,amsgrad=False)
    train(model, optimizer,train_dataloader,test_dataloader,epochs=1000) 
     
