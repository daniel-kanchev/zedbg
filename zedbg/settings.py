BOT_NAME = 'zedbg'
SPIDER_MODULES = ['zedbg.spiders']
NEWSPIDER_MODULE = 'zedbg.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'zedbg.pipelines.DatabasePipeline': 300,
}