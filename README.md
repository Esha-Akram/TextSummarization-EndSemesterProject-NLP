## seq2seq
Universal sequence-to-sequence model with attention and beam search for inference decoding. Should work for text summarization, 
neural machine translation, question generation etc. although might require different hyperparameters or data preprocessing.

## Text-Summarization using Seq2Seq Model 
In jupyter notebook file, I'v trained model on News Summary Dataset from KAGGLE which have Original Text and Summary columns.


## Installation
pip install tensorflow
pip install torch
pip install pandas
pip install spacy
spacy.load("en_core_web_sm")
pip install matplotlib
pip install numpy
pip install scikit-learn

## Deploy with Flask
pip install tensorflow==2.5.0

## Model Architecture
Let’s consider a simple example to understand how Attention Mechanism works:

Source sequence: “Which sport do you like the most?
Target sequence: “I love cricket”
The first word ‘I’ in the target sequence is connected to the fourth word ‘you’ in the source sequence, right? Similarly, the second-word ‘love’ in the target sequence is associated with the fifth word ‘like’ in the source sequence.

So, instead of looking at all the words in the source sequence, we can increase the importance of specific parts of the source sequence that result in the target sequence. This is the basic idea behind the attention mechanism.

There are 2 different classes of attention mechanism depending on the way the attended context vector is derived:

Global Attention
Local Attention
Let’s briefly touch on these classes.

Global Attention
Here, the attention is placed on all the source positions. In other words, all the hidden states of the encoder are considered for deriving the attended context vector:

Global attention
Source: Effective Approaches to Attention-based Neural Machine Translation – 2015
Local Attention
Here, the attention is placed on only a few source positions. Only a few hidden states of the encoder are considered for deriving the attended context vector:

local attention
Source: Effective Approaches to Attention-based Neural Machine Translation – 2015
We will be using the Global Attention mechanism in this article.

## Usage
To run the project, follow these steps:

Ensure that you have installed all the required dependencies, including TensorFlow, Keras, and any other relevant libraries. You can refer to the "Installation" section for detailed instructions on installing the dependencies.

Open a command prompt or terminal and navigate to the project directory.

Run the following command to start the application:

python app.py
This command will start the web server and make the application accessible through a local URL.

Once the application is running, you can access it through your web browser. Open your preferred browser and enter the following URL:

http://localhost:5000
The web interface will be displayed, allowing you to interact with the text analysis and summarization functionality.

Input Text Formats:

The application supports various input text formats, including plain text files, URLs, or direct text input through the web interface. Here are examples of how to provide input in different formats:

Plain Text File:

Prepare a text file containing the input text you want to analyze or summarize.
Click the "Choose File" button on the web interface and select the text file from your local system.
The application will read the contents of the file and perform the analysis or generate the summary.
URL:

Copy the URL of a webpage or article that you want to analyze or summarize.
Paste the URL into the provided text input field on the web interface.
The application will fetch the content from the URL and process it accordingly.
Direct Text Input:

If you prefer, you can directly enter the text you want to analyze or summarize into the provided text input field on the web interface.
Simply type or paste the text into the text input field, and the application will process it accordingly.
Limitations and Known Issues:

It is important to note the following limitations and known issues of the project:

The application may have a maximum limit on the length of input text it can process effectively. Very long documents or texts exceeding this limit may not produce accurate summaries or analysis results.

The quality of the generated summaries heavily depends on the complexity and nature of the input text. Summaries for highly technical or domain-specific content may not be as accurate or comprehensive.

The application's performance and response time may vary depending on the hardware and resources available on the system running the application.

If using the web interface, ensure that you have a stable internet connection to fetch content from URLs or external sources.

If you encounter any issues or have suggestions for improvement, please refer to the "Future Improvements" section in the README file for instructions on providing feedback or contributing to the project.

Please customize the above details according to your project's specific requirements and limitations.

## Dataset
The dataset consists of 4515 examples and contains Author_name, Headlines, Url of Article, Short text, Complete Article. I gathered the summarized news from Inshorts and only scraped the news articles from Hindu, Indian times and Guardian. Time period ranges from febrauary to august 2017.
## Inspiration
Generating short length descriptions(headlines) from text(news articles).
Summarizing large amount of information which can be represented in compressed space
## Acknowledgements
I would like to thank the authors of Inshorts for their amazing work

## Results

## License
GPL 2

## Examples
Review: irish deputy prime minister frances fitzgerald announced her resignation on tuesday in bid to avoid the collapse of the government and potential snap election she quit hours before no confidence motion was to be proposed against her by the main opposition party the political crisis began over fitzgerald role in police whistleblower scandal 
Original summary: start irish deputy prime minister resigns to avoid govt collapse end 
Predicted summary:  start i am not to be in the film industry end

## References
https://www.analyticsvidhya.com/blog/2019/06/comprehensive-guide-text-summarization-using-deep-learning-python/#h-implementing-text-summarization-in-python-using-keras

