from employees import Employee
from companies import Company

kurt_krafft = Employee("Kürt Krafft", "UI/UX Engineer", "6/27/2020")
sofia_candiani = Employee("Sofia Candiani", "Software Developer", "6/27/2020")
cooper_nichols = Employee("Cooper Nichols", "Back-End Engineer", "6/27/2020")
matt_kroeger = Employee("Matthew Kroeger", "Front-End Developer", "6/27/2020")
mike_prince = Employee("Joseph Prince", "Software Engineer 1", "6/27/2020")

lyft = Company("Lyft", "401 Church St.", "Transportation")
tdot = Company("Tennessee Department Of Transportation", "505 Deaderick St.", "Government Administration")

lyft.hire(kurt_krafft)
tdot.hire(sofia_candiani)
lyft.hire(cooper_nichols)
tdot.hire(matt_kroeger)
lyft.hire(mike_prince)

lyft.generate_report()

tdot.generate_report()