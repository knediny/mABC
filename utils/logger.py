import logging


def setup_logging(log_file_path, log_name='my_logger'):
    # 创建一个logger
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)  # 设置最低的log级别

    # 创建一个文件处理器，将log写入文件
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)  # 设置文件处理器的log级别

    # 创建一个控制台处理器，将log输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # 设置控制台处理器的log级别

    # 创建一个格式化器，定义log的格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将处理器添加到logger中
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    log_file_path = "example.log"

    # 设置logging
    logger = setup_logging(log_file_path)

    # 记录一些log
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
