import json
import os
tasks = []
next_id = 1

def save_tasks():
	with open("tasks.json", "w", encoding="utf-8") as f:
		json.dump(tasks, f, ensure_ascii=False, indent=2)

def load_tasks():
	global tasks, next_id
	if os.path.exists("tasks.json"):
		with open("tasks.json", "r", encoding="utf-8") as f:
			tasks = json.load(f)
		if tasks:
			next_id = max(task['id'] for task in tasks) + 1
		else:
			next_id = 1
	else:
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

def update_task():
	if not tasks:
		print("\nยังไม่มีงานในรายการ")
		return
	print("\n--- แก้ไขงาน ---")
	for idx, task in enumerate(tasks, start=1):
		status = 'เสร็จแล้ว' if task['completed'] else 'ยังไม่เสร็จ'
		print(f"{idx}. {task['title']} (ครบกำหนด: {task['due_date']}, สถานะ: {status})")
	try:
		index = int(input("เลือกหมายเลขงานที่ต้องการแก้ไข: "))
		if index < 1 or index > len(tasks):
			print("ลำดับไม่ถูกต้อง!")
			return
	except ValueError:
		print("กรุณาป้อนตัวเลข!")
		return
	task = tasks[index-1]
	print(f"\n--- แก้ไขงาน: {task['title']} ---")
	new_title = input(f"ชื่อเรื่องใหม่ (Enter เพื่อข้าม): ")
	new_description = input(f"รายละเอียดใหม่ (Enter เพื่อข้าม): ")
	new_status = input(f"สถานะ (1=เสร็จแล้ว, 0=ยังไม่เสร็จ, Enter เพื่อข้าม): ")
	if new_title:
		task['title'] = new_title
	if new_description:
		task['description'] = new_description
	if new_status == '1':
		task['completed'] = True
	elif new_status == '0':
		task['completed'] = False
	print("แก้ไขงานสำเร็จ!")

def delete_task():
	if not tasks:
		print("\nยังไม่มีงานในรายการ")
		return
	print("\n--- ลบงาน ---")
	for idx, task in enumerate(tasks, start=1):
		status = 'เสร็จแล้ว' if task['completed'] else 'ยังไม่เสร็จ'
		print(f"{idx}. {task['title']} (ครบกำหนด: {task['due_date']}, สถานะ: {status})")
	try:
		index = int(input("เลือกหมายเลขงานที่ต้องการลบ: "))
		if index < 1 or index > len(tasks):
			print("ลำดับไม่ถูกต้อง!")
			return
	except ValueError:
		print("กรุณาป้อนตัวเลข!")
		return
	task = tasks[index-1]
	confirm = input(f"ต้องการลบงาน '{task['title']}' จริงหรือไม่ (y/n): ").strip().lower()
	if confirm == 'y':
		del tasks[index-1]
		print("ลบงานสำเร็จ!")
	else:
		print("ยกเลิกการลบงาน")

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
			update_task()
		elif choice == '4':
			delete_task()
		elif choice == '5':
			print("ออกจากโปรแกรม...")
			save_tasks()
			break
		else:
			print("กรุณาเลือกเมนู 1-5 เท่านั้น!")

if __name__ == "__main__":
	load_tasks()
	main_menu()
