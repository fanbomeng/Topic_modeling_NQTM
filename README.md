# Code for Short Text Topic Modeling with Topic Distribution Quantization and Negative Sampling Decoder

[PDF](https://www.aclweb.org/anthology/2020.emnlp-main.138.pdf)


## Usage
### 0. Prepare environment

For exact package version, please refer to the environment.yml file

requirements:

    python==3.6
    tensorflow-gpu==1.13.1
    scipy==1.5.2
    scikit-learn==0.23.2 


### 1. Prepare data

Note: the data should be preprocessed with tokenization, filtering non-Latin characters, etc before.

       function is in utils/input_preprocessing.py

 

python utils/preprocess.py --path data/stackoverflow --output_dir input/stackoverflow


### 2. Run the modeli


    In the main file run_NQTM, there are a set of parameters can be tuned, like number of topics, model hidden layer dimension. 
    Two main function to be called:
    1) print_tpic_words: this function will select topic and associated words for that topic for each of the document. two parameter:
		A) n_topic_selection=2  number of topic selected 
		B) n_top_words=2        in each of the topic how many words to be kept
    2) print_top_words, print all of the selected topic words in the model 


    two data sets can be used, one is stackoverflow, the other is Calculus 


    python run_NQTM.py --data_dir input/stackoverflow --output_dir output


### 3. Evaluation

topic coherence: [coherence score](https://github.com/dice-group/Palmetto).

topic diversity:

    python utils/TU.py --data_path output/top_words_T15_K50_1th


