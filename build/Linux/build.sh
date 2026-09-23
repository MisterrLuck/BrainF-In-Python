chmod +x brain

cp brain ~/.local/bin/
echo "Making bash file"

cd ../../
cp -r src/ ~/.local/bin/
cd ~/.local/bin
mv src/ brainf_src/

echo "Creating source code"

echo "Type 'brain' followed by your file name, to run BrainF***"
