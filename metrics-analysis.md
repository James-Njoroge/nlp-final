### README: Evaluation Process Using NLPScholar Outputs

To evaluate our model’s performance in distinguishing “interesting” vs. “not interesting” matches, we will leverage NLPScholar's automated output capabilities to generate our metrics, including accuracy, precision, recall, and F1 score. 
NLPScholar provides outputs in TSV format that capture detailed prediction data, such as model predictions, true labels, and specific conditions or contexts. 
We can leverage and directly calculate these metrics, offering a quantitative assessment of the model’s effectiveness in capturing match interest.

The evaluation process will involve loading NLPScholar’s prediction files and using `analyze` mode compute metrics, or even using visualizations if we can. 
Using the true and predicted labels within these TSV files, we will calculate accuracy, which shows the proportion of correct predictions, as well as precision, recall, and F1 score to assess balanced performance. 
Confusion matrices will also be generated to provide a breakdown of true positives, true negatives, false positives, and false negatives, allowing us to pinpoint areas of strength and improvement. 
These metrics and the confusion matrix can be easily summarized in tables or visualized as figures, providing a holistic view of the model’s predictive ability.

In addition to quantitative metrics, we will analyze specific cases where the model misclassified matches, using these insights to guide future adjustments. 
For instance, we’ll examine whether certain misclassifications stem from overfitting to technical terms or misinterpretation of sentiment within the commentary. 
This process ensures that we gain both quantitative and qualitative feedback from NLPScholar's outputs, enabling us to gain insights about our work and next steps.
