import jinja2
import os
import csv

template_file = "switch.j2"
csv_parameter_file = input("Enter parameter-file to convert: ")
config_parameters = []
output_directory = "output"
print(csv_parameter_file[:-4])

print("Read CSV parameter file...")
with open(csv_parameter_file, 'r') as f:
    reader = csv.reader(f)
    interfaces = list(reader)

print("Create Jinja2 environment...")
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."))
template = env.get_template(template_file)
result = template.render(data=interfaces[1::])

print(result)


if not os.path.exists(output_directory):
    os.mkdir(output_directory)

print("Create templates...")

f = open(os.path.join(output_directory, csv_parameter_file[:-4] + ".txt"), "w")
f.write(result)
f.close()
print("Configuration '%s' created..." % csv_parameter_file[:-4] + ".txt")
print("DONE")
