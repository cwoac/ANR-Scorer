"""Main Entry point for ANR Scorer"""

import logging
import tkinter as Tk
import tkinter.scrolledtext as ScrolledText
import tkinter.ttk as ttk

import ANRS


class ANRScorer:
    def __init__(self, root):
        self.root = root
        self.log = ANRS.logger()
        self.log.setLevel(logging.WARN)

        logger_frame = ttk.Frame(root)
        logger_frame.pack(fill=Tk.X, expand=Tk.Y)
        ttk.Label(logger_frame, text="Log:").pack(side=Tk.LEFT)
        self.loggerLevel = ttk.Combobox(
            logger_frame,
            state="readonly",
            value=['debug', 'infomation', 'warning', 'error'])
        self.loggerLevel.bind("<<ComboboxSelected>>", self.change_log_level)
        self.loggerLevel.current(2)
        self.loggerLevel.pack(side=Tk.LEFT)
        log_frame = ttk.Frame(root)
        log_frame.pack(fill=Tk.X, expand=Tk.Y)
        logger = ScrolledText.ScrolledText(
            log_frame,
            state=Tk.DISABLED,
            height=5, )
        logger.pack(fill=Tk.BOTH, expand=Tk.Y, side=Tk.BOTTOM)
        ANRS.setLoggerConsole(logger)

    def change_log_level(self, event):
        levels = [logging.DEBUG, logging.INFO, logging.WARN, logging.ERROR]
        ANRS.logger().info("Setting log level to %s"
                           % levels[self.loggerLevel.current()])
        ANRS.logger().setLevel(levels[self.loggerLevel.current()])

def main():
    root = Tk.Tk()
    root.wm_title("ANR Scorer")
    ANRScorer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
