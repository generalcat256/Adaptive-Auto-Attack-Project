# Adaptive-Auto-Attack-Project
In this GitHub repository I sought to recreate the results from the paper and corresponding GitHub repository, Practical Evaluation of Adversarial Robustness via Adaptive Auto Attack. I include a possible improvement over the methods described in the paper as part of our assignment. The paper has a corresponding github repository available here: https://github.com/liuye6666/adaptive_auto_attack. This github repository's code is designed to run a small experiment similar to the demonstration provided in the original git repository in addition to testing the possible improvement I implemented for the purpose of the assignment. spirit


# Step by Step Guide:
You can download the code in this github to your python IDE of choice using the following command: 

```
git clone https://github.com/liuye6666/adaptive_auto_attack.git

%cd adaptive_auto_attack

!pip install torch torchvision pandas numpy tqdm pillow -q
```

The model that this github repository is designed to run is available in the github and does not have to be downloaded from an external source. 


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

# System Requirements: 
I personally ran this code using google colab pro. You can also run it on university available computational clusters
like Unity. Overall the code is designed to run on windows so you will most likely have to do a lot of troubleshooting
if you try to run it on site on mac hardware. You will get cuda errors. 
