tasks = []
next_id = 1

def add_task():
	global next_id
	print("\n--- เพิ่มงานใหม่ ---")
	title = input("ชื่อเรื่อง: ")
	description = input("รายละเอียด: ")
	due_date = input("วันครบกำหนด (YYYY-MM-DD): ")
	task = {
		'id': next_id,
		'title': title,
		'description': description,
		'due_date': due_date,
		'completed': False
	}
	tasks.append(task)
	print(f"เพิ่มงานสำเร็จ (ID: {next_id})")
	next_id += 1

def view_tasks():
	print("\n--- รายการงานทั้งหมด ---")
	if not tasks:
		print("ยังไม่มีงานในรายการ")
		return
	print(f"{'ลำดับ':<6}{'ชื่องาน':<20}{'วันครบกำหนด':<15}{'สถานะ':<12}")
	for idx, task in enumerate(tasks, start=1):
		status = 'เสร็จแล้ว' if task['completed'] else 'ยังไม่เสร็จ'
		print(f"{idx:<6}{task['title']:<20}{task['due_date']:<15}{status:<12}")

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
