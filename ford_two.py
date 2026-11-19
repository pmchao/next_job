import re


class LogEntry:
    def __init__(
        self,
        timestamp: str,
        level: str,
        component: str,
        message: str
    ):
        self.timestamp = timestamp
        self.level = level
        self.component = component
        self.message = message

    def __str__(self):
        return (
            f"{self.timestamp} "
            f"[{self.level}] "
            f"{self.component}: {self.message}"
        )


def parse_log_line(line: str, cls: type[LogEntry]):
    pattern = (
        r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
        r'(?P<level>\w+) '
        r'(?P<component>[^:]+): '
        r'(?P<message>.+)$'
    )

    match = re.fullmatch(pattern, line)

    if not match:
        return None

    return cls(**match.groupdict())


def main():
    line = (
        "2026-10-15 10:30:45 ERROR "
        "Database: Connection timeout"
    )

    entry = parse_log_line(line, LogEntry)

    if entry:
        print(entry)
        print(entry.level)
        print(entry.message)


if __name__ == "__main__":
    main()