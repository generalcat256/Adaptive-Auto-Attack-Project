# Adaptive-Auto-Attack-Project
In this GitHub repository I sought to recreate the results from the paper and corresponding GitHub repository, Practical Evaluation of Adversarial Robustness via Adaptive Auto Attack. I include a possible improvement over the methods described in the paper as part of our assignment. The paper has a corresponding github repository available here: https://github.com/liuye6666/adaptive_auto_attack. This github repository's code is designed to run a small experiment similar to the demonstration provided in the original git repository in addition to testing the possible improvement I implemented for the purpose of the assignment. My idea was as follows. The paper assumes: loss alone measures difficulty but this ignores whether the attack is still improving. My idea was to incorporate progress of the attack. This was achieved using the following formulation:

Score = current loss + 𝜆 (current loss – previous loss) 

Current loss describes how easily attackable an image is now. Current loss – previous loss describes how much progress we have made in attacking the image since the last step. It was my hope that this way we would be attacking images that are already high in loss, but also images that are still improving, or where the attack is still working. I also explored different scoring strategies (pre selections) namely, loss, log loss, confidence, margin. Confidence measures how certain the model is in the correct class, while margin measures how close the model is to predicting a different class. Margin is often more informative because it directly reflects how close the input is to the decision boundary. I did use GPT to patch the code of the original paper with this new formulation, and commented the code to demonstrate my understanding of the major components!

# Step by Step Guide:
You can download the code in this github to your python IDE of choice using the following command: 

```
git clone https://github.com/generalcat256/Adaptive-Auto-Attack-Project.git

cd Adaptive-Auto-Attack-Project

pip install torch torchvision numpy pandas tqdm pillow
```

The model that this github repository is designed to run is available in the github and does not have to be downloaded from an external source. 
In order to run the standard baseline experiment as presented in the original git repository run the following command: 

```
python Adaptive_Auto_Attack_main.py
```

In order to run the experimental suite I designed use the following command: 

```
python run_experiments.py
```

This runs the following experiments and provides a clear table with clean accuracy, robust accuracy, and runtime: 

baseline AAA

progress-lambda scoring with lambda = 0.25

progress-lambda scoring with lambda = 0.50

preselection using loss

preselection using log-loss

preselection using confidence

preselection using margin


# Software packages:
We used the following software packages. 

Pytorch

torchvision

numpy

pandas

tqdm

pillow

Optional: 
-opencv-python (for image processing if needed)

# Models: 
For the purpose of this demonstration this github attacks a TRADES-mnist trained model which is a small-CNN. 
Full host of models is available in the following link https://pan.baidu.com/s/1_pKv2OBGplSvoNNYdYBJgA

Extraction Code: arej

Note you may need a mainland Chinese phone number in order to gain full access. 

# Results: 

<img width="1179" height="375" alt="Screenshot 2026-04-28 at 11 06 45 PM" src="https://github.com/user-attachments/assets/f30cffe6-b900-4790-823f-71b3c0db27b1" />


# System Requirements: 
I personally ran this code using google colab pro. You can also run it on university available computational clusters
like Unity. Overall the code is designed to run on windows so you will most likely have to do a lot of troubleshooting
if you try to run it on site on mac hardware. You will get cuda errors. 
