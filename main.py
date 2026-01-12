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
	pass

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
			update_task()
		elif choice == '4':
			delete_task()
		elif choice == '5':
			print("ออกจากโปรแกรม...")
			break
		else:
			print("กรุณาเลือกเมนู 1-5 เท่านั้น!")

if __name__ == "__main__":
	main_menu()
