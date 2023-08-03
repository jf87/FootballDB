# Training Code/Instruction
## Valuenet

The codebase for and a tutorial on how to train ValueNet is available here: https://github.com/brunnurs/valuenet 

## T5 
The T5 model which has been trained on the Spider Dataset and used in our zero shot experiments can be found here: https://huggingface.co/tscholak/cxmefzzi

This model was then fined tuned (no changes were made to the T5 trainer) on the FootballDB data. 

## T5 + Picard 
The code for running the evaluation of T5 with Picard is available here: https://github.com/yizhang-unifr/picard

In addtion to the original [Picard code](https://github.com/ServiceNow/picard), the repo also contains the following elements, which were used for our FootballDB evaluations: 
  * Execution accuracy on PostgreSQL DB
  * Dataset pipe for FootballDB
  * DeepSpeed z2-configurations for running on multiple GPUs


