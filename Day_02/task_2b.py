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


def problem_dampener(report):
    return any(is_save(report[:i] + report[i + 1:]) for i in range(len(report)))

if __name__ == "__main__":
    reports = load_reports("puzzle_input.txt")
    total = 0
    for report in reports:
        if not is_save(report):
            total += problem_dampener(report)
        else:
            total += 1

    print(total)
