from pprint import pprint

def read_input(filename):
    input_data = {}
    #Length of the schedule
    length_of_schedule = 0

    #Number of Employees
    number_of_employees = 0

    ##Number of Shifts
    number_of_shifts = 0

    # Temporal Requirements Matrix Shifts per Days
    temporal_requirements_matrix = []

    #ShiftName, Start, Length, MinlengthOfBlocks, MaxLengthOfBlocks
    shift_name, start_shift, length_shift, min_length_of_blocks, max_length_of_blocks \
        = [], [], [], [], []

    # Minimum and maximum length of days-off blocks 
    min_days_off = 0
    max_days_off = 0 

    # Minimum and maximum length of work blocks
    min_length_work_blocks = 0
    max_length_work_blocks = 0

    # Number of not allowed shift sequences: NrSequencesOfLength2, NrSequencesOfLength3: 
    nr_sequences_of_length_2 = 0
    nr_sequences_of_length_3 = 0

    # Not allowed shift sequences 
    not_allowed_shif_sequences = [
        ['N', 'D'], ['N', 'A'], ['A', 'D']
    ]
    with open(filename, 'r') as f:
        lines = iter(f.readlines())
        for line in lines:
            if "#Length of the schedule" in line:
                length_of_schedule = int(next(lines))
            if "#Number of Employees" in line:
                number_of_employees = int(next(lines))
            if "##Number of Shifts" in line:
                number_of_shifts = int(next(lines))
            if "# Temporal Requirements Matrix" in line:
                ns = number_of_shifts
                temporal_requirements_matrix = []
                for i in range(number_of_shifts):
                    temporal_requirements_matrix.append(list(map(int, next(lines).split())))
            if "#ShiftName" in line:
                ns = number_of_shifts
                shift_name, start_shift, length_shift, min_length_of_blocks, max_length_of_blocks \
                    = ['-']*ns, [0]*ns, [0]*ns, [0]*ns, [0]*ns
                for i in range(number_of_shifts):
                    shift_name[i], start_shift[i], length_shift[i], min_length_of_blocks[i], max_length_of_blocks[i] = next(lines).split()
                    start_shift[i], length_shift[i] = list(map(int, start_shift[i])), list(map(int, length_shift[i]))
                min_length_of_blocks, max_length_of_blocks = [int(x) for x in min_length_of_blocks], [int(x) for x in max_length_of_blocks] 
            if "# Minimum and maximum length of days-off blocks" in line:
                min_days_off, max_days_off = list(map(int, next(lines).split()))
            if "# Minimum and maximum length of work blocks" in line:
                min_length_work_blocks, max_length_work_blocks = list(map(int, next(lines).split()))
            if "# Number of not allowed shift sequences: NrSequencesOfLength2, NrSequencesOfLength3:" in line:
                nr_sequences_of_length_2, nr_sequences_of_length_3 = list(map(int, next(lines).split()))
            if "# Not allowed shift sequences" in line:
                not_allowed_shift_sequences_2, not_allowed_shift_sequences_3 = [], []
                for i in range(nr_sequences_of_length_2):
                    not_allowed_shift_sequences_2.append(next(lines).split('\n')[0].split())
                for i in range(nr_sequences_of_length_3):
                    not_allowed_shift_sequences_3.append(next(lines).split('\n')[0].split())

    input_data = {
        'length_of_schedule': length_of_schedule,
        'number_of_employees': number_of_employees,
        'number_of_shifts': number_of_shifts, 
        'temporal_requirements_matrix': temporal_requirements_matrix,
        'shift_name': shift_name,
        'start_shift': start_shift,
        'length_shift': length_shift,
        'min_length_of_blocks': min_length_of_blocks,
        'max_length_of_blocks': max_length_of_blocks,
        'min_days_off': min_days_off,
        'max_days_off': max_days_off,
        'min_length_work_blocks': min_length_work_blocks,
        'max_length_work_blocks': max_length_work_blocks,
        'nr_sequences_of_length_2': nr_sequences_of_length_2,
        'nr_sequences_of_length_3': nr_sequences_of_length_3,
        'not_allowed_shift_sequences_2': not_allowed_shift_sequences_2,
        'not_allowed_shift_sequences_3': not_allowed_shift_sequences_3    
    }

    return input_data 

pprint(read_input('rws_instances/Example1.txt'))
pprint(read_input('rws_instances/Example4.txt'))