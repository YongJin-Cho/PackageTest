choice = int(input())

if   choice == 1: import packageTest.subpackage1.moduleX as mod
elif choice == 2: import packageTest.subpackage1.moduleY as mod
elif choice == 3: import packageTest.subpackage2.moduleX as mod
elif choice == 4: import packageTest.subpackage2.moduleX as mod
else:             import packageTest.moduleZ as mod

mod.test()
