def load_reports(filename):
    reports = []
    with open(filename, "r") as f:
        for report in f.readlines():
            report = report.strip().split(" ")
            report = list(map(int, report))
            reports.append(report)
    return reports


def is_save(report):
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False

    if len(set(report)) != len(report):
        return False

    return all(abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))


if __name__ == "__main__":
    reports = load_reports("puzzle_input.txt")
    total = 0
    for report in reports:
        total += is_save(report)
    print(total)
