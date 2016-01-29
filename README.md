cf-python-test-app-fastpush
===

This sample app illustrates the cf-fastpush CloudFroundry CLI plugin. [fastpush](https://github.com/xiwenc/cf-fastpush-plugin)
enables developers to update their CloudFoundry hosted application at lightning
speed:

```bash
git clone https://github.com/xiwenc/cf-python-test-app-fastpush.git
cd cf-python-test-app-fastpush
cf install-plugin cf-fastpush-plugin
time cf push samplefastpush
#
# Using manifest file /home/xcheng/git/cf-python-test-app/manifest.yml
#
# ...
#
# #0   running   2016-01-29 09:31:06 PM   0.0%   15.7M of 128M   114.9M of 256M

#cf push samplefastpush  1.88s user 1.91s system 5% cpu 1:04.55 total

# Change the file a bit
vim hello.py

# repush with fast-push
time cf fast-push samplefastpush
# warning: dry run not set, commencing fast push
# Running the fast-push command
# Target app: samplefastpush
#
# [MOD] hello.py
# [NEW] manifest.yml
# Restarting after updating 2 files

# cf fast-push samplefastpush  0.40s user 0.05s system 7% cpu 5.667 total
```
