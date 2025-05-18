menu = -1

while menu != 0:
    print("\n Main Menu")
    print("1. PhoneBook")
    print("2. Messages")
    print("3. Chat")
    print("4. Call register")
    print("5. Tones")
    print("6. Settings")
    print("7. Call divert")
    print("8. Games")
    print("9. Calculator")
    print("10. Reminders")
    print("11. Clock")
    print("12. Profiles")
    print("13. SIM Services")
    print("0. Exit")

    menu = int(input("Enter a number: "))

    if menu == 1:
        phoneBookOption = -1
        while phoneBookOption != 0:
            print("\nPhone book: ")
            print("1. Search")
            print("2. Service No.s")
            print("3. Add Name")
            print("4. Erase")
            print("5. Edit")
            print("6. Assign tone")
            print("7. Send b'card")
            print("8. Options")
            print("0. Back")
            phoneBookOption = int(input("Select an option: "))

            if phoneBookOption == 8:
                options = -1
                while options != 0:
                    print("\nOptions: ")
                    print("1. Type of view")
                    print("2. Memory Status")
                    print("0. Back")
                    options = int(input("Select an option: "))
                    if options == 1:
                        print("Type of view selected.")
                    elif options == 2:
                        print("Memory Status selected.")

    elif menu == 2:
        messageOption = -1
        while messageOption != 0:
            print("\nMessages: ")
            print("1. Write Messages")
            print("2. Inbox")
            print("3. Outbox")
            print("4. Picture Messages")
            print("5. Templates")
            print("6. Smileys")
            print("7. Message Settings")
            print("8. Info Service")
            print("9. Voice Mailbox Number")
            print("10. Service Command Editor")
            print("0. Back")
            messageOption = int(input("Select an option: "))

            if messageOption == 7:
                messageSettings = -1
                while messageSettings != 0:
                    print("\nMessage Settings: ")
                    print("1. Message center Number")
                    print("2. Message sent as:")
                    print("3. Message Validity")
                    print("0. Back")
                    messageSettings = int(input("Select an option: "))

                commonSettings = -1
                while commonSettings != 0:
                    print("\nCommon: ")
                    print("1. Delivery Reports")
                    print("2. Reply via same centre")
                    print("3. Character Support")
                    print("0. Back")
                    commonSettings = int(input("Select an option: "))

    elif menu == 3:
        print("Chat selected.")

    elif menu == 4:
        callRegisterOption = -1
        while callRegisterOption != 0:
            print("\nCall Register: ")
            print("1. Missed Calls")
            print("2. Received Calls")
            print("3. Dialled numbers")
            print("4. Erase recent call lists")
            print("5. Show call duration")
            print("0. Back")
            callRegisterOption = int(input("Select an option: "))

            if callRegisterOption == 5:
                callDurationOption = -1
                while callDurationOption != 0:
                    print("\nCall Duration: ")
                    print("1. Last Call duration")
                    print("2. All call duration")
                    print("3. Received calls' duration")
                    print("4. Dialled calls duration")
                    print("5. Clear timers")
                    print("0. Back")
                    callDurationOption = int(input("Select an option: "))

    elif menu == 5:
        tonesOption = -1
        while tonesOption != 0:
            print("\nTones: ")
            print("1. Ringing Tone")
            print("2. Ringing Volume")
            print("3. Incoming Call Alert")
            print("4. Composer")
            print("5. Message Alert tone")
            print("6. Keypad Tones")
            print("7. Warning and game tones")
            print("8. Vibrating alert")
            print("9. Screen saver")
            print("0. Back")
            tonesOption = int(input("Select an option: "))

    elif menu == 6:
        settingsOption = -1
        while settingsOption != 0:
            print("\nSettings: ")
            print("1. Call settings")
            print("2. Phone settings")
            print("3. Security settings")
            print("4. Restore Factory Settings")
            print("0. Back")
            settingsOption = int(input("Select an option: "))

            if settingsOption == 1:
                print("1. Automatic redial")
                print("2. Speed dialing")
                print("3. Call waiting operations")
                print("4. Own number sending")
                print("5. Phone line in use")
                print("6. Automatic answer")

            elif settingsOption == 2:
                print("\nPhone Settings:")
                print("1. Language")
                print("2. Cell Info Display")
                print("3. Welcome Note")
                print("4. Network selection")
                print("5. Lights")
                print("6. Confirm SIM service Actions")

            elif settingsOption == 3:
                print("\nSecurity Settings:")
                print("1. PIN code request")
                print("2. Call barring request")
                print("3. Fixed dialling")
                print("4. Closed user group")
                print("5. Phone security")
                print("6. Change Access codes")

    elif menu == 7:
        print("Call divert selected.")

    elif menu == 8:
        print("Games selected.")

    elif menu == 9:
        print("Calculator selected.")

    elif menu == 10:
        print("Reminders selected.")

    elif menu == 11:
        clockOption = -1
        while clockOption != 0:
            print("\nClock: ")
            print("1. Alarm Clock")
            print("2. Clock Settings")
            print("3. Date Settings")
            print("4. Stopwatch")
            print("5. Countdown timer")
            print("6. Auto update of date and time")
            print("0. Back")
            clockOption = int(input("Select an option: "))

    elif menu == 12:
        profileSelection = -1
        while profileSelection != 0:
            print("Profiles.")
            print("0. back")
            profileSelection = int(input())

    elif menu == 13:
        simSelection = -1
        while simSelection != 0:
            print("SIM Services.")
            print("0. back")
            simSelection = int(input())

    elif menu == 0:
        print("Thank you for using Nokia 3310")

    else:
        print("Invalid selection, try again.")
