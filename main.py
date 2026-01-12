def add_task():
	pass

def view_tasks():
	pass

def edit_task():
	pass

def delete_task():
	pass

def main_menu():
	while True:
		print("\n===== ToDoList Menu =====")
		print("1. เพิ่มงานใหม่")
		print("2. ดูงานทั้งหมด")
		print("3. แก้ไขงาน")
		print("4. ลบงาน")
		print("5. ออกจากโปรแกรม")
		choice = input("เลือกเมนู (1-5): ")
		if choice == '1':
			add_task()
		elif choice == '2':
			view_tasks()
		elif choice == '3':
			edit_task()
		elif choice == '4':
			delete_task()
		elif choice == '5':
			print("ออกจากโปรแกรม...")
			break
		else:
			print("กรุณาเลือกเมนู 1-5 เท่านั้น!")

if __name__ == "__main__":
	main_menu()
