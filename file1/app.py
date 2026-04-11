





from datetime import datetime
import os
import shutil
from ftplib import FTP
import ftplib
import socket
 # section 1 lets you input Credentials for the FTP server aslo check to for invalid Credentials
while True:
 ftp = FTP()
 file_credentials1 = []
 print("please enter host num,port num, username, password")
 print("all seperated by commas")
 host_portsuser_pass = input()
 host_portsuser_pass_copy = host_portsuser_pass
 file_credentials1.append(host_portsuser_pass)
 join_credentials1 = "".join(file_credentials1)
 spliting_credentials1 = join_credentials1.split(",")
 print(spliting_credentials1)
 try:
  ftp.connect(spliting_credentials1[0],int(spliting_credentials1[1]))
  login = ftp.login(spliting_credentials1[2], spliting_credentials1[3])
 except ConnectionRefusedError:

   print("invalid port number out of range")
 except ftplib.error_perm:

   print("invalid the username or password is inccorect")
 except IndexError:

   print("invalid Credentials")
 except ValueError:

   print("invalid port number must be an integer")
 except socket.gaierror:
   
   print("invalid host number, must look like this 123.0.0.1")
 else:
   break
print(login)
 # end of section 1
 # section 2 checks for valid folder path for mixed files 
print("please insert folder path")
while True:
    folder_path = input().replace('"', '')
    try:
        if not os.path.isdir(folder_path):
            raise FileNotFoundError(f"Folder not found: {folder_path}")
    except FileNotFoundError:
        print("please input valid file path")
    else:
        break

print(f"{folder_path} valid file path")
  # end of section 2
  # section 3 checks for valid folder path for good files 

switching_box2 = []

switching_box = []

def re_run():
 print("please insert folder path for good files")
 while True:
  good_folder = input().replace('"', '')
  try:
   if not os.path.isdir(good_folder):
    raise FileNotFoundError(f"Folder not found: {good_folder}")
  except FileNotFoundError:
   print("please input valid file path")
  else:
    switching_box.append(good_folder)
    break  
  
 print(f"{good_folder} valid file path")
 return good_folder 
re_run()
  # end of section 3
  # section 4 checks for valid folder path for bad files
def re_run2():
 print("please insert folder path for bad files")
 while True:
  bad_folder = input().replace('"', '')
  try:
     if not os.path.isdir(bad_folder):
      raise FileNotFoundError(f"Folder not found: {bad_folder}")
  except FileNotFoundError:
     print("please input valid file path")
  else:
     switching_box2.append(bad_folder)
     break
   
 return bad_folder 
re_run2()
   # end of section 4
   # section 5 makes sure the good and bad file paths are diffrent  
while True:
 if switching_box  ==  switching_box2:
  switching_box.clear()
  switching_box2.clear()
  print("good and bad path cannot be the same")
  re_run()
  re_run2()
 else:
  print("all folder paths are valid")
  all_good_paths = switching_box
  break

def check_for_invalid_date():
 path_one = switching_box[0]

 path_two = switching_box2[0]
 file_path = os.listdir(f"{folder_path}")
  # end of section 5
 for i in file_path:
        file_path = os.path.join(folder_path, i)
        file_path_copy = file_path
    # section 6 reads file name and strips file name of everything but numbers
        file_name = os.path.basename(file_path)
        num_date = file_name.split("_")
        date_part = num_date[2]
        num_date = date_part.split(".")
        date = num_date[0]
    # end of section 6

    # section 7 separates the date in to individual year, month, day, hour, minute, second items

        year = int(date[0:4])

        month = int(date[4:6])

        day = int(date[6:8])

        hour = int(date[8:10])

        minute = int(date[10:12])

        second = int(date[12:14])

    # end of section 7

    # section 8 tells you if the date is invalid or not
        bad_key = []
        try:
            datetime(year, month, day, hour, minute, second)
        except ValueError:
            bad_key.append("invalid wrong date")
        else:
            pass
        # end of section 8
        # section 9 opens and reads the file
        open_file = open(file_path)

        reads_file = open_file.read()

        open_file.close()
    # end of section 9
    # section 10 appends the file contents to a list
        byte0_file = [""]

        unknown_byte_file = []

        unknown_byte_file.append(reads_file)
    # end of section 10
    # section 11 lets you know if the file is empty or not
        not_empty = []
        while True:
            if unknown_byte_file == byte0_file:
                bad_key.append("invalid empty")
                break
            else:
                not_empty.append("trigger")
                break
    # end of section 11

        if  not_empty == ['trigger']:
    # section 12 opens and reads the file
            open_file2 = open(file_path_copy)

            read_file = open_file2.read()
            
            open_file2.close()
    # end of section 12
    # section 13 appends the commas of the file to a list
            comma_amount = []
            unused_numbers = []
            swiching_missing_colums = []

            for i in read_file:
                if i == (","):
                    comma_amount.append(i)
                elif i != (","):
                    unused_numbers.append(i)
                else:
                    break
    # end of section 13
    # section 14 tells you if the file is malformed or not
            total_commas = len(comma_amount)
            while True:
                if total_commas == 121:
                    swiching_missing_colums.append("trigger 1")
                    break
                elif total_commas != 121:
                    bad_key.append("invalid malformed")
                    break  
            if swiching_missing_colums == ['trigger 1']:
    # end of section 14
    # section 15 opens,and strips the file of whitespaces
              open_file3 = open(file_path_copy)

              file_contents4 = open_file3.read()

              open_file3.close()
              clean_contents = file_contents4.strip()
    # end of section 15

    # section 16 splits the contents by cammos and strips it of emptystrings
              split_comma = clean_contents.split(",")

              no_emptystring = [i.strip() for i in split_comma if i.strip()]

              without_headers = " ".join(no_emptystring)

              split_items = without_headers.split()
    # end of section 16

    # section 17 determines if there is any items missing
              tenth_column = len(split_items[120:132])
    # end of section 17

    # section 18 lets you know if there is anything missing
              correct_columns = 12
              no_missing_items = []
              while True:
                  if tenth_column != correct_columns:
                     bad_key.append("invalid missing colums")
                     break
                  else:
                    no_missing_items.append('trigger 2')
                    break
    # end of section 18
              if no_missing_items == ['trigger 2']:
    # section 19 opens,reads, and strips the file
                open_file4 = open(file_path_copy)
                   
                file_contents = open_file4.read()
                
                open_file4.close()

                clean_contents = file_contents.strip()
    # end of section 19
    # section 20 splites the headers into individual varibles 
                headings = clean_contents[0:109]

                only_headings = headings

                total_headers = []

                batch_header = only_headings[0:8]

                timestamp_header = only_headings[9:18]

                reading1_header = only_headings[19:27]

                reading2_header = only_headings[28:36]

                reading3_header = only_headings[37:45]

                reading4_header = only_headings[46:54]

                reading5_header = only_headings[55:63]

                reading6_header = only_headings[64:72]

                reading7_header = only_headings[73:81]

                reading8_header = only_headings[82:90]

                reading9_header = only_headings[91:99]

                reading10_header = only_headings[100:109]
                
    # end of section 20
    # section 21 checks for invalid headers 
                total_headers = []
                while_trigger = []
                while True:
                    if (
                        batch_header == ("batch_id")
                        and timestamp_header == ("timestamp")
                        and reading1_header == ("reading1")
                        and reading2_header == ("reading2")
                        and reading3_header == ("reading3")
                        and reading4_header == ("reading4")
                        ):
                        total_headers.append("correct")
                        break
                    else:
                        while_trigger.append("wrong")
                        break
                
                while True:
                    if (
                        reading5_header == ("reading5")
                        and reading6_header == ("reading6")
                        and reading7_header == ("reading7")
                        and reading8_header == ("reading8")
                        and reading9_header == ("reading9")
                        and reading10_header == ("reading10")
                        ):
                        total_headers.append("correct")
                        break
                    else:
                        while_trigger.append("wrong")
                        break
                     
                header_amount = len(total_headers)

    # end of section 22
    # section 23 tells you if all headers are correct in the file
                correct_amount = 2

                while True:
                    if header_amount == correct_amount:
                        #switching_id.append("good headers")
                        pass
                        break
                    else:
                        bad_key.append("invalid headers")
                        pass
                        break
                    
                open_file5 = open(file_path_copy)

                file_contents = open_file5.read()

                open_file5.close()

                clean_contents = file_contents.strip()
    # end of section 23
    # section 24 splites each item individually and removes \n
                split_headers = clean_contents.split()

                rejoin_numbers = " ".join(split_headers)

                split_comma = rejoin_numbers.split(",")

                join_contents = " ".join(split_comma)

                single_items = join_contents.split()
    # end of section 24

    # section 25 gets rid of batch ids,headers, and timestamps

                readings = []
                non_readings = []

                for i in single_items:
                     try:
                      float(i)
                      readings.append(i)
                     except ValueError:
                            non_readings.append(i)
                     else:
                        pass

                floats = []
                batch_ids = []
                for i in readings:
                        if i == readings[0]:
                            batch_ids.append(i)
                        elif i == readings[11]:
                            batch_ids.append(i)
                        elif i == readings[22]:
                            batch_ids.append(i)
                        elif i == readings[33]:
                            batch_ids.append(i)
                        elif i == readings[44]:
                            batch_ids.append(i)
                        elif i == readings[55]:
                            batch_ids.append(i)
                        elif i == readings[66]:
                            batch_ids.append(i)
                        elif i == readings[77]:
                            batch_ids.append(i)
                        elif i == readings[88]:
                            batch_ids.append(i)
                        elif i == readings[99]:
                            batch_ids.append(i)
                        else:
                            floats.append(i)
    # end of section 25
    # section 26 turns the strings in to floats and sorts valid and invalid floats
                readings_floats = [float(i) for i in floats]

                incorrect_floats = []

                correct_floats = []
                for i in readings_floats:
                        if i >= 9.9:
                            incorrect_floats.append(i)
                        elif i < 9.9:
                            correct_floats.append(i)
                        else:
                            break
    # end of section 26
    # section 27 telled you if floats are good or not 
                while True:
                        if incorrect_floats != []:
                            bad_key.append("invalid floats")
                            break
                        else:
                            pass
                            break
    # end of section 27
    # section 28 chedcks for invalid batch ids
                expected_amount = len(batch_ids)

                id_numbers = batch_ids


                def check_duplicates():
                 total_index = len(id_numbers)
                 remaning_checks = total_index

                 current_index = len(id_numbers)
                 switch_index = 1
                 results_of_check = []
                 copy_notused = []

                 while True:
                    if current_index != 0 and remaning_checks != 0:
                      current_index = current_index-switch_index
                      current_item = id_numbers[current_index]
                      current_id = current_item
                      remaning_checks = remaning_checks - 1
                      for i in id_numbers:
                         if i != current_id:
                          copy_notused.append(1)
                         elif i == current_id:
                          results_of_check.append(0)
                      current_id = None
                    else:
                      break
                 return results_of_check
    # end of section 28
 
                check_duplicates()
    #section 28 tell you if batch ids are valid or not 
                result_amount = len(check_duplicates())

                while True:
                 if result_amount == expected_amount:
                     pass
                     break
                 elif result_amount != expected_amount:
                     bad_key.append("invalid ids")
                     break
    # end of section 28
              else:
                  pass 
            else:
                pass
        else:
           pass
    # section 29 moves good and bad files to seprate folders
        if bad_key == []:
            print("good")
            shutil.move(file_path_copy, path_one)
        elif bad_key != []:
            print("bad")
            shutil.move(file_path_copy, path_two)
        

check_for_invalid_date()        
    # end of section 29