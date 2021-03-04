#installing conda environment
conda create -n cv --clone base
conda activate cv
pip install --upgrade pip
pip install opencv-python
pip install --upgrade tensorflow
pip install jupyter

#setting up our Jupyter notebook for this course
git clone https://github.com/damioune123/computer_vision_crash_course.git
cd computer_vision_crash_course
jupyter notebook

