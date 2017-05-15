# filtertool

```sh
% pip install git+https://github.com/otiai10/filtertool.git
% which filtertool
```

```sh
% filtertool -i your.pileup -o result.vcf \
  --depth 20  \ # filter depth more than 20
  --count 6   \ # filter variant count more than 6
  --freq  0.5 \ # filter variant frequency more than 0.5
  --verbose   \ # display progress on stderr
  --trial     \ # try it only for first 100000 lines of input
  # if you provide multi samples, you can specify algorithm to filter them
  --alg fishers,p=0.8

........................................................................................................................................................................................................100000
FOUND: 38

% less result.vcf # <- this is what you want ;)
```
