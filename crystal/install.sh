#!/bin/bash

versions=("0.35.1" "0.36.0" "1.0.0")

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    urls=(
        "https://github.com/elbywan/crystalline/releases/download/v0.1.9/crystalline_linux.gz" \
        "https://github.com/elbywan/crystalline/releases/download/v0.2.1/crystalline_x86_64-unknown-linux-gnu.gz" \
        "https://github.com/elbywan/crystalline/releases/download/v0.3.0/crystalline_x86_64-unknown-linux-gnu.gz"\
    )
elif [[ "$OSTYPE" == "darwin"* ]]; then
    urls=(
        "https://github.com/elbywan/crystalline/releases/download/v0.1.9/crystalline_darwin.gz" \
        "https://github.com/elbywan/crystalline/releases/download/v0.2.1/crystalline_x86_64-apple-darwin.gz" \
        "https://github.com/elbywan/crystalline/releases/download/v0.3.0/crystalline_x86_64-apple-darwin.gz"\
    )
else
    echo Unable to probe OS version, or your OS is not supported.
    exit 1
fi

output=$(crystal --version)
if [[ -z output ]]
then
    echo There is an error looking for Crystal version. Possibly, Crystal is not installed
    exit 2
fi

output=($output)
if [[ ${output[0]} != "Crystal" ]]
then
    echo Unable to find Crystal version in crystal output
    exit 3
fi

version=${output[1]}
echo Found Crystal version $version

url=""
for key in ${!versions[@]}
do
     if ! [[ "$version" < "${versions[$key]}" ]]
     then
         url=${urls[$key]}
     fi
done

if [[ -z $url ]]
then
    echo Unable to find crystalline URL for your Crystal version
    exit 4
fi

echo Using URL $url

if command -v wget &> /dev/null
then
    wget -q --show-progress $url -O /tmp/crystalline.gz
elif command -v curl &> /dev/null
then
    curl -L $url -o /tmp/crystalline.gz
else
    echo Error: you need either wget or curl to download crystalline
    exit 5
fi

gzip -df /tmp/crystalline.gz
chmod +x /tmp/crystalline
mv -f /tmp/crystalline /usr/local/bin/
