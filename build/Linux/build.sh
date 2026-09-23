# dir=$(pwd)

cp brainf.sh ~/.brainf.sh
echo "Making bash file"

cd ../../
cp -r src/ ~/.brainf/
echo "Creating source code"
cd ~/

# mv src .brainf
# mv brainf.sh .brainf.sh
mv .brainf.sh .brainf/

echo "source ~/.brainf.sh" >> .bashrc
echo "Running language runner"

echo "Type 'brain' followed by your file name, to run BrainF***"
source ~/.bashrc
# cd $dir
