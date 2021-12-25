		
import os
from stat import S_IWRITE

class Antivirus:
	"""An antivirus program that detect, remove, and recover (if possible) 
	python files infected by the PyCrash virus.

	attribute: current_path - a path where the antivirus scans by default
	(the current path where this filename is residing)
	"""
	current = os.path.abspath(os.path.dirname(__file__))

	def __init__(self, path=current):
		self.current_path = path
		
	def quick_scan(self):
		"""Quick Scan: scan the current path recursively to find infected python files"""
		print("-"*80)
		print("\tQuick Scannig the current path... " + self.current_path)
		print("-"*80)
		path_to_scan = self.current_path
		infected_files = self.scan(path_to_scan)
		print("\nFinished: Collecting scan results...\n")
		print("\n" + "-"*33 + " Scan Results " + "-"*33)

		if len(infected_files) == 0:
			print("\nCongratulations... No Virus detected!\n")
			print("-"*80)
		else:
			print("\n Notice... The following files are infected by PyCrash virus.\n")
			print("-"*80)
			self.take_action(infected_files)

	def custom_scan(self):
		"""Custom Scan: scan the given path recursively to find infected python files"""
		print("-"*80)
		print("\tCustom Scannig... ")
		print("-"*80)
		path_to_scan = self.accept_path()
		infected_files = self.scan(path_to_scan)
		print("\nFinished: Collecting scan results...\n")
		print("\n" + "-"*33 + " Scan Results " + "-"*33)

		if len(infected_files) == 0:
			print("\nCongratulations... No Virus detected!\n")
			print("-"*80)
		else:
			print("\n Notice... The following files are infected by PyCrash virus.\n")
			print("-"*80)
			self.take_action(infected_files)

	def full_scan(self):
		"""Full Scan: scan the whole computer to find infected python files"""
		print("-"*80)
		print("\tFull Scannig the computer. This might take a long time...")
		print("-"*80)
		path_to_scan = "E:/"
		infected_files = self.scan(path_to_scan)
		print("\nFinished: Collecting scan results...\n")
		print("\n" + "-"*33 + " Scan Results " + "-"*33)

		if len(infected_files) == 0:
			print("\nCongratulations... No Virus detected!\n")
			print("-"*80)
		else:
			print("\n Important! The following files are infected by PyCrash virus.\n")
			print("-"*80)
			self.take_action(infected_files)

	def take_action(self, infected_files):
		"""Take action on infected files"""
		count = 1
		for filename in infected_files:
			print(str(count) + " " + filename)
			count += 1
		print("\nActions you can take.")
		print("\t1 -> remove file (permanently delete)")
		print("\t2 -> recover file (only if possible)")
		print("\t3 -> take no action (allow on this device)")

		print("\nTo take action on files...\n" +
			"--- enter the number in front of the filename to select single file\n"+
			"--- or space separated list of numbers to select multiple files\n"+
			"--- enter * to select all files then\n"+
			"--- enter the action you want take.\nFor example\n"+
			"File(s): 1 2 means select file on line 1 and line 2.\nFile(s): * means select all files.")

		ch = input("\nContiue to take action? (y/n): ")
		while ch == 'y':
			files = input("\nFile(s): ")

			if files[0] != "*":
				files = [(int(i)-1) for i in files.split(" ")]

			action = input("Action: ") # the action the user wants to take

			if action == '1':
				# remove file
				if files == '*':
					ch = input("Are you sure you want to permanently delete all files? (y/n): ")
					if ch == "y" or ch == "Y":
						self.remove(infected_files)
				elif len(files) >= 1:
					files_selected = []
					for file_number in files:
						files_selected.append(infected_files[file_number])
					self.remove(files_selected)
				else:
					print("Wrong file selection. Please select the correct file.")
			elif action == '2':
				if files == '*':
					ch = input("Are you sure you want to recover all files? (y/n): ")
					if ch == "y" or ch == "Y":
						self.recover(infected_files)
				elif len(files) >= 1:
					files_selected = []
					for file_number in files:
						files_selected.append(infected_files[file_number])
					self.recover(files_selected)
				else:
					print("Wrong file selection. Please select the correct file.")
			elif action == '3':
				print("\nWarning: allowing this infected files may damage your files.")
			else:
				print("Wrong command!")
			ch = input("Contiue to take action? (y/n): ")
		print("\nThank you for using Aflem Antivirus")

	def remove(self, filelist):
		"""Delete the given files from the computer permanently"""
		for file in filelist:
			os.chmod(file , S_IWRITE) # to get WRITE permission
			os.remove(file)
			print(file + " ... has been permanently deleted.")

	def recover(self, filelist):
		"""Recover the original content of the file if possible"""
		for filename in filelist:
			file_content = open(filename)
			orginal_content = "" # the orginal content to be extracted from the infected file
			for i, line in enumerate(file_content):
				if i >= 83:
					orginal_content += line

			with open(filename, 'w') as f:
				os.chmod(filename , S_IWRITE) # to get WRITE permission
				f.write(orginal_content)
			print(filename + " ... has been recovered successfully.")

	def is_infected(self, filename):
		"""Checks whether the given file is infected by the virus or not"""
		# signature.txt contains symptoms that a file may be infected by virus
		suspected = 0
		for line in open(filename):
			for sign in open("signature.txt"):
				if sign.strip() in line:
					suspected += 1
				if suspected >= 7:
					return True
		return False

	def scan(self, path):
		"""Searchs the given path recursively to find infected python files"""
		infected_files = [] # the list of .py files that are infected
		filelist = os.listdir(path) # the list of files in the current path
		for fname in filelist:
			full_path = os.path.join(path, fname)
			if os.path.isdir(full_path):
				infected_files.extend(self.scan(full_path))
			elif fname[-3:] == ".py":
				print("Scanning...\t" + full_path)
				if self.is_infected(full_path):
					infected_files.append(full_path)
		return infected_files

	def accept_path(self):
		"""Accepts a valid path from the user to scan"""
		print("Enter the full path. E.g 'C:/Users/Alex/Documents' without quotes.")
		path = input()

		if os.path.exists(path):
			return path
		else:
			print("\nThe path you specified does not exist. Try another\n")
			self.accept_path()

	def show_menu(self):
		"""Different scan options available"""
		print("\nChoose Scan Options:-\n")
		print("1 -> Quick Scan\n\tChecks the folders where threats are commonly found.")
		print("2 -> Custom Scan\n\tChoose which files and locations you want to check.")
		print("3 -> Full Scan\n\tChecks all files on your hard disk. This scan could take"+
			" longer than 1 hour.")
		print("0 -> Exit the program")
		
	def run(self):
		"""Runs the antivirus program"""
		#print("~"*100)
		#print("\t\tAflem Antivirus 21.0")
		print("~"*100)
		print("""
    #                                      #                                                 
   # #   ###### #      ###### #    #      # #   #    # ##### # #    # # #####  #    #  ####  
  #   #  #      #      #      ##  ##     #   #  ##   #   #   # #    # # #    # #    # #      
 #     # #####  #      #####  # ## #    #     # # #  #   #   # #    # # #    # #    #  ####  
 ####### #      #      #      #    #    ####### #  # #   #   # #    # # #####  #    #      # 
 #     # #      #      #      #    #    #     # #   ##   #   #  #  #  # #   #  #    # #    # 
 #     # #      ###### ###### #    #    #     # #    #   #   #   ##   # #    #  ####   ####
 """)
		print("~"*100)
                                                                                             

		self.show_menu()
		choice = int(input("\nScan option: "))
		if choice != 0:
			if choice in [1, 2, 3]:
				if choice == 1:
					self.quick_scan()
				elif choice == 2: 
					self.custom_scan()
				elif choice == 3:
					self.full_scan()
			else:
				print("Please enter the correct choice.")
		else:
			print("\nGood bye. Come back later to scan your computer.\n")

def main():
	if __name__ == "__main__":
		Aflem = Antivirus()
		Aflem.run()

main()
