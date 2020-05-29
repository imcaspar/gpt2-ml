curl -o ~/miniconda.sh -O https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh
chmod +x ~/miniconda.sh
~/miniconda.sh -b -p ~/conda
rm ~/miniconda.sh
~/conda/bin/conda install -y python=3.7
~/conda/bin/conda init // exit shell

conda create -n gpt3 python=3.7


sudo apt install parallel
pip install ujson==2.0.3

export PYTHONPATH=$(pwd) //project path