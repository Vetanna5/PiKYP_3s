class Software:
    def __init__(self, id, title, developer, size_mb, computer_id):
        self.id = id
        self.title = title
        self.developer = developer
        self.size_mb = size_mb
        self.computer_id = computer_id


class Computer:
    def __init__(self, id, model):
        self.id = id
        self.model = model


class Installation:
    def __init__(self, computer_id, software_id):
        self.computer_id = computer_id
        self.software_id = software_id

computers = [
    Computer(1, 'Apple_Macbook-01'),
    Computer(2, 'Lenovo-02'),
    Computer(3, 'Apple_Macbook-03'),
    Computer(4, 'hp-04'),
    Computer(5, 'Apple_Macbook-05'),
]

software_list = [
    Software(1, 'Текстовый редактор', 'Иванов', 250, 1),
    Software(2, 'Графический редактор', 'Петров', 480, 1),
    Software(3, 'Архиватор', 'Сидоров', 35, 2),
    Software(4, 'Веб-браузер', 'Смирнов', 320, 2),
    Software(5, 'Среда разработки', 'Кузнецова', 650, 3),
    Software(6, 'Медиаплеер', 'Орлов', 180, 4),
    Software(7, 'Антивирус', 'Волков', 210, 5),
]

installations = [
    Installation(1, 1),
    Installation(1, 2),
    Installation(1, 5),
    Installation(2, 2),
    Installation(2, 3),
    Installation(2, 4),
    Installation(3, 1),
    Installation(3, 5),
    Installation(3, 6),
    Installation(4, 3),
    Installation(4, 4),
    Installation(4, 6),
    Installation(5, 1),
    Installation(5, 7),
]


def make_one_to_many():
    records = []
    for computer in computers:
        for software in software_list:
            if software.computer_id == computer.id:
                records.append((software, computer))
    return records


def make_many_to_many():
    software_by_id = {software.id: software for software in software_list}
    computer_by_id = {computer.id: computer for computer in computers}
    records = []

    for installation in installations:
        computer = computer_by_id.get(installation.computer_id)
        software = software_by_id.get(installation.software_id)
        if computer is not None and software is not None:
            records.append((software, computer))

    return records


def show_developer_programs(one_to_many):
    print('Задание Д1')
    result = [
        (software.title, computer.model)
        for software, computer in one_to_many
        if software.developer.endswith('ов')
    ]
    print(result)

def show_average_sizes(one_to_many):
    print('\nЗадание Д2')
    average_sizes = []

    for computer in computers:
        sizes = [
            software.size_mb
            for software, linked_computer in one_to_many
            if linked_computer.id == computer.id
        ]

        if sizes:
            average_sizes.append((computer.model, sum(sizes) / len(sizes)))

    average_sizes.sort(key=lambda record: record[1])
    print(average_sizes)


def show_programs_on_a_computers(many_to_many):
    print('\nЗадание Д3')
    result = {}

    for computer in computers:
        if computer.model.startswith('A'):
            installed_titles = [
                software.title
                for software, linked_computer in many_to_many
                if linked_computer.id == computer.id
            ]
            result[computer.model] = installed_titles

    print(result)


def main():
    one_to_many = make_one_to_many()
    many_to_many = make_many_to_many()

    show_developer_programs(one_to_many)
    show_average_sizes(one_to_many)
    show_programs_on_a_computers(many_to_many)


if __name__ == '__main__':
    main()
