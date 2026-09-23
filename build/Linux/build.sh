chmod +x brain

cp brain ~/.local/bin/brain
echo "Making bash file"

cd ../../
cp -r src/ ~/.local/bin/brainf_src/
echo "Creating source code"
cd ~/

echo "Type 'brain' followed by your file name, to run BrainF***"
