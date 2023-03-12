# Crawl sierra


crawl sierra.com to buy specific product in discount


```

# set environment
SLACK_HOOK_URL=...

# set cronjob
* * * * * cd ~/path_to/crawl_sierra && python3.9 crawl.py >> ~/path_to_log/crawl.log 2>&1
```
