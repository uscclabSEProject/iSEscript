# This python file transfer USER prefix type record to csv file
import csv
import auparse

AUDIT_LOG_FILE = "audit.log"
AUDIT_USER_CSV = "audit.user.csv"

# get all field
au = auparse.AuParser(auparse.AUSOURCE_FILE, AUDIT_LOG_FILE )
all_field_names = []
au.parse_next_event()
while True:
    while True:
        if au.get_field_name() == "type" and "USER_" in au.get_field_str():
            while True:
                field_name = au.get_field_name()
                field_content = au.get_field_str()
                if not field_name in all_field_names:
                    all_field_names.append(field_name)

                if not au.next_field(): break
        if not au.next_record(): break
    if not au.parse_next_event(): break

# write to csv file
au = auparse.AuParser(auparse.AUSOURCE_FILE, AUDIT_LOG_FILE )
csvfile = open(AUDIT_USER_CSV, 'w+')
writer = csv.DictWriter(csvfile, fieldnames=all_field_names)
writer.writeheader()

fields = {} 
au.parse_next_event()

# iterate event
while True:
    # iterate record
    while True:
        if au.get_field_name() == "type" and "USER_" in au.get_field_str():
            fields = {}
            # iterate field
            while True:
                field_name = au.get_field_name()
                field_content = au.get_field_str()
                fields[field_name] = field_content

                if not au.next_field(): break

            writer.writerow(fields)

        if not au.next_record(): break
    if not au.parse_next_event(): break
