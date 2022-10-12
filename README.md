
### Research Papers
1. Deep Learning-Powered Prediction of Human-Virus Protein-Protein Interactions(Dec-2021):<br/>
<pre>
	a. Negative sampling: Dissimilarity-Based Negative Sampling(A->B(sequence similarity > Threshold) , B->C(positive interaction) then A and C cannot be negative sample)
	b. Dataset imabalalance recommended to replicate real world scenario: 1:10 (has been proven reasonable to predict PPI)						
	c. Word2vec, Doc2vec and Node2vec
	d. Train on large human PPI, and later fine tune on specific PPI(eg. Human-SARs-Cov-2 PPIs)
	e. DeepVHPPI: First trained on supervised structure prediction, and then fine tune for PPI
	f. Alphafold-2 could be used for PPI 
</pre>
![alt text](images/ppi_table.png)

2. Deep Viral: prediction of novel virus-host interactions from protein sequences and infectious disease phenotypes(April-2021):<br/>
<pre>
	a. Dataset sources: HPIDB, String, SARS-CoV-2 interatcions #332 PPI from 27 viral proteins(https://www.nature.com/articles/s41586-020-2286-9, Protein sequences retrieved from swiss-prot db)
        b. Negative sampling:
		i.) Dissimilarity-Based Negative Sampling
		ii.) randomly sample from postive sample and sequences similarity < 80 percent  
        c. Dataset imabalalance recommended to replicate real world scenario: 1:>2 (has been proven reasonable to predict PPI)
        d. Phenotype features + Sequences
        e. DL2Vec, W2V
        f. Keep test set completely different than train set(to prevent data leakage)
        g. Evaluation dataset sufferrs from several drawbacks
	h. Dataset szie: 24,678 positive interactions and 1,066 viral protein from 14 virus families and 292 virus taxa(length<=1000)
	 
</pre>
![alt text](images/DeepViral_workflow.png)
3. DWPPI- A Deep Learning Approach for predicting PPI in plants based multi-source information with a large scale biological network(March-2022):<br/>
<pre>
        a. Dataset sources: Plant PPIs
        b. Negative sampling:
                i.) randomly sample   
        c. Dataset balance
        d. Bipartite graph + deepwalk --> CBOW-W2V(4-mer) --> 64 Dim -->LR,DT,
        e. Dataset size: 28110+81989+51514  positive interactions 

</pre>
4. Transfer Learning via multi-scale convolutional neural layers for human-virus ppi prediction(16 July-2021):<br/>
<pre>
        a. Dataset sources: HPIDB, VirHostNet, VirusMentha, PHISTO, and PDB                                                                                                                    
        b. Dataset Target for fine-tuning: human-SARS-CoV-2-PPIs(568)
	c. Dataset construction procedure:
		i.) Remove ppi which detected only once
	       ii.) Remove non-physical interactions
	      iii.) Remove interaction between proteins without PSSM features	
	c. Negative sampling:
                i.) randomly sample--> Dissimlarity based negative sampling  
        c. Dataset imbalance(1:10)
	d. 5-fold CV                                                                                                   
        e. sequences -->PSSMs(Sequence profile)-->embedded vectors-->siamese CNN --> MLP --> prediction score 
        f. Dataset size: 31,381(9880 in HIV, 5966 in Herpes, 5099 in Papilloma, 3044 in Influenze, 1300 in Hepatitis, 927 in Dengue, 709 in Dengue)                                                                              
	g. Accuracy: 93%
	i. Dataset available: https://github.com/XiaodiYangCAU/TransPPI/tree/main/sample
	j. Ensemble of 5 models(AvgX)
	k. Intersting to read how they divided dataset and fine tuned it and also the result analysis part
</pre>

![alt text](images/Transfer_learning_ppi.png)

5. LSTM-PHV: prediction of human-virus protein-protein interactions by LSTM with word2vec:<br/>
<pre>
    a.Here we cloned, tagged and expressed 26 of the 29
	  SARS-CoV-2 proteins in human cells and identifed the human proteins that physically
	  associated with each of the SARS-CoV-2 proteins using afnity-purifcation mass spectrometry,
	  identifying 332 high-confdence protein–protein interactions between SARS-CoV-2 and human proteins
	b. Database: HPIDB 3.0
	        How dataset was created?
				--> MI score >= 0.3 are kept. MI score is the confidence score assigned to each PPI from <b>Intact</b> and <b>VirHostnet</b>
				--> Redundant PPIs were excluded by using CD-HIIT with an identity threshold of 0.95
				--> Removed proteins of length less than 30 and more than 1000<b>(30 <= len(proteins) <= 1000)</b>
	c. Negative sampling:
			Dissimilarity based negative sampling method: Read Denovo paper and this paper again for full understanding
														Really nice way to do it
	c. Dataset size: 22,383 positive pairs (5882 human and 996 virus proteins) 
	c. Dataset and API: http://kurata35.bio.kyutech.ac.jp/LSTM-PHV/introduction_page
</pre>




5. A SARS-CoV-2 protein interaction map reveals targets for drug repurposing(Nature articles-Gold Standard):<br/>
<pre>
    a.Here we cloned, tagged and expressed 26 of the 29
	  SARS-CoV-2 proteins in human cells and identifed the human proteins that physically
	  associated with each of the SARS-CoV-2 proteins using afnity-purifcation mass spectrometry,
	  identifying 332 high-confdence protein–protein interactions between SARS-CoV-2 and human proteins
	b. MIST> 0.75
	c. SARS sequence from GenScript
</pre>

6. ProteinNet: a standardized dataset for ml of protein structure<br/>
<pre>
    a. Based on sequence identity
</pre>
	
### Database Information
1. HPIDB 2.0: 45,238 manually curated entries PPI
2. HVIDB: 48,643 experimentally verified human–virus PPIs covering 35 virus families, 6633 virally targeted host complexes, 3572 host
dependency/restriction factors as well as 911 experimentally verified/predicted 3D complex structures of human–virus PPIs.
Furthermore, our database resource provides tissue-specific expression profiles of 6790 human genes that are targeted by
viruses and 129 Gene Expression Omnibus series of differentially expressed genes post-viral infections(Collected) 

### Dataset Information





### Models



### Task with date



