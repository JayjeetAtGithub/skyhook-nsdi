1. Clone the SkyhookDM repository.
```bash
git clone https://github.com/uccross/skyhookdm-arrow
cd skyhookdm-arrow/
```

2. Run the SkyhookDM container in interactive mode.
```bash
docker run -it -v $PWD:/w -w /w --privileged uccross/skyhookdm-arrow:v0.2.0 bash
```

3. Install docker.
```bash
curl -o- https://get.docker.com | bash
```

3. Run the build script.
```bash
./build.sh
```

4. Run the tests script.
```bash
./test.sh
```
