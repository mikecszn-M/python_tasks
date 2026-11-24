import textwrap


def show(text):
    """Print a triple-quoted block with the common indentation removed
    (like a Java text block)."""
    print(textwrap.dedent(text))


def main():
    show("""\
        List of Menu Functions
        1.Phone book
        2.Messages
        3.Chat
        4.Call register
        5.Tones
        6.Settings
        7.Call divert
        8.Music
        9.Games
        10.Calculator
        11.Reminders
        12.Clock
        13.Profiles
        14.Services
        15.SIM services

        Please input the chosen number to access the menu:
        """)

    option = int(input())

    match option:
        case 1:
            show("""\
                Welicome to Phone book Menu
                1.Search
                2.Service Nos
                3.Add name
                4.Erase
                5.Edit
                6.Copy
                7.Assign tone
                8.Send b'card
                9.Options
                10.Speed dials
                11.Voice tags

                Please input your chosen number to access the menu:
                """)

            option1 = int(input())

            match option1:
                case 1: print("Welicome to Search option")
                case 2: print("You picked Service Nos option")
                case 3: print("You picked Add name option")
                case 4: print("You are choosing to erase")
                case 5: print("You are in Edit Function")
                case 6: print("Welicome to Copy option")
                case 7: print("Welicome to Assign tone option")
                case 8: print("Welicome to Send b'card option")
                case 9:
                    show("""\
                        Welicome to Options, please choose any option below
                        1.Memory in use
                        2.Type of view
                        3.Memory status

                        Please input your chosen number to access the menu:
                        """)

                    option12 = int(input())

                    match option12:
                        case 1: print("You are in Memory in use options")
                        case 2: print("You are in Type of view options")
                        case 3: print("You are in Memory status options")
                        case _: print("Invalid option")
                case 10: print("You are in Speed dials option")
                case 11: print("You are in Voice tags option")
                case _: print("Invalid option")

        case 2:
            show("""\
                Welicome to Message Menu
                1.Write Message
                2.Inbox
                3.Outbox
                4.Picture messages
                5.Templates
                6.Smileys
                7.Message settings
                8.Info service
                9.Voice mailbox number
                10.Service command editor

                Please input your chosen number to access the menu:
                """)

            option2 = int(input())

            match option2:
                case 1: print("Welicome to Write messages option")
                case 2: print("You picked Inbox option")
                case 3: print("You picked Outbox option")
                case 4: print("You are choosing to enter Picture messages")
                case 5: print("You are in Templates Function")
                case 6: print("Welicome to Smileys option")
                case 7:
                    show("""\
                        Welicome to Message settings option, please pick any option below
                        1.Set 1
                        2.Common

                        Please input the number to access the message settings option:
                        """)

                    option21 = int(input())

                    match option21:
                        case 1:
                            show("""\
                                Welicome to Set 1
                                1.Message centre number
                                2.Message sent as
                                3.Message validity

                                Please input the number to access Set 1 option:
                                """)

                            option22 = int(input())

                            match option22:
                                case 1: print("Welicome to Message centre number")
                                case 2: print("Welicome to Message sent as option")
                                case 3: print("Welicome to Message validity option")
                                case _: print("Invalid option")
                        case 2:
                            show("""\
                                Welcome to Common
                                1.Delivery reports
                                2.Reply via same centre
                                3.Character support

                                Please input the number to access Common option:
                                """)

                            option23 = int(input())

                            match option23:
                                case 1: print("Welicome to Delivery reports option")
                                case 2: print("Welicome to Reply via same centre option")
                                case 3: print("Welicome to Character support option")
                                case _: print("Invalid option")
                        case _: print("Invalid option")
                case 8: print("Welicome to Info service option")
                case 9: print("Welicome to Voice mailbox number option")
                case 10: print("You are in Service command editor option")
                case _: print("Invalid option")

        case 3:
            print("Welicome to Chat")

        case 4:
            show("""\
                Welcome to Call register
                1. Missed calls
                2. Received calls
                3. Dialled numbers
                4. Erase recent call lists
                5. Show call duration
                6. Show call costs
                7. Call cost settings
                8. Prepaid credit

                Enter the corresponding number to access that Call register option:
                """)

            option24 = int(input())

            match option24:
                case 1: print("Welcome to Missed calls")
                case 2: print("Welcome to Received calls")
                case 3: print("Welcome to Dialled numbers")
                case 4: print("Welcome to Erase recent call lists")
                case 5:
                    show("""\
                        Welcome to Show call duration
                        1. Last call duration
                        2. All calls’ duration
                        3. Received calls’ duration
                        4. Dialled calls’ duration
                        5. Clear timers
                        """)
                    option25 = int(input())

                    match option25:
                        case 1: print("Welicome to Last call duration")
                        case 2: print("Welicome to All calls’ duration")
                        case 3: print("Welicome to Received calls’ duration")
                        case 4: print("Welicome to Dialled calls’ duration")
                        case 5: print("Welicome to Clear timers")
                case 6:
                    show("""\
                        Welicome to Show call costs
                        1. Last call cost
                        2. All calls’ cost
                        3. Clear counters
                        """)
                    option26 = int(input())

                    match option26:
                        case 1: print("Welicome to Last call cost")
                        case 2: print("Welicome to All calls’ cost")
                        case 3: print("Welicome to Clear counters")
                case 7:
                    show("""\
                        Welicome to Call cost settings
                        1. Call cost limit
                        2. Show costs in
                        """)
                    option27 = int(input())

                    match option27:
                        case 1: print("Welcome to Call cost limit")
                        case 2: print("Welcome to Show costs in")
                case 8: print("Welcome to Prepaid credit")

        case 5:
            show("""\
                Welcome to Tones
                1. Ringing tone
                2. Ringing volume
                3. Incoming call alert
                4. Message alert tone
                5. Keypad tones
                6. Warning tones
                7. Vibrating alert
                8. Screen saver

                Please input a  number to access that Tones Options Menu:
                """)

            option5 = int(input())

            match option5:
                case 1: print("This is Ringing tone option")
                case 2: print("Welicome to Ringing volume")
                case 3: print("You are in Incoming call alert Menu")
                case 4: print("Welicome to Message alert tone")
                case 5: print("Welicome to Keypad tones")
                case 6: print("This is Warning tones Menu")
                case 7: print("Welicome to Vibrating alert")
                case 8: print("Welicome to Screen saver")

        case 6:
            show("""\
                Welucome to Settings
                1. Call settings
                2. Phone settings
                3. Security settings
                4. Restore factory settings

                Please put number to access that Settings options:
                """)

            option6 = int(input())

            match option6:
                case 1:
                    show("""\
                        Welucome to Call settings
                        1. Automatic redial
                        2. Speed dialling
                        3. Call waiting options
                        4. Own number sending
                        5. Phone line in use
                        6. Automatic answer

                        Please input number to access that Call settings options:
                        """)
                    option61 = int(input())

                    match option61:
                        case 1: print("You are in Automatic redial Menu")
                        case 2: print("Welucome to Speed dialling Menu")
                        case 3: print("Welucome to Call waiting options")
                        case 4: print("Welicome to Own number sending")
                        case 5: print("Welcome to Phone line in use Option")
                        case 6: print("Welcome to Automatic answer Option")
                case 2:
                    show("""\
                        Welucome to Phone settings
                        1. Language
                        2. Cell info display
                        3. Welcome note
                        4. Network selection
                        5. Confirm SIM service actions

                        Please input a number to access that Phone settings options:
                        """)
                    option62 = int(input())

                    match option62:
                        case 1:
                            show("""\
                                Welcome to Language
                                There's nothing to do here sorry
                                """)
                        case 2:
                            show("""\
                                Welcome to Cell info display
                                There's nothing to do here sorry
                                """)
                        case 3: print("Welicome to Welcome note")
                        case 4: print("Welicome to Network selection")
                        case 5: print("Welcome to Confirm SIM service actions")
                case 3:
                    show("""\
                        You have arrived at Security settings options
                        1. PIN code request
                        2. Call barring service
                        3. Fixed dialling
                        4. Closed user group
                        5. Security level
                        6. Change access codes

                        Provide a number to access that Security settings Options:
                        """)
                    option63 = int(input())

                    match option63:
                        case 1: print("Welcome to PIN code request")
                        case 2: print("Welicome to Call barring service")
                        case 3: print("Welicome to Fixed dialling")
                        case 4: print("Welicome to Closed user group")
                        case 5: print("Welucome to Security level")
                        case 6: print("Welucome to Change access codes")
                case 4:
                    print("This menu is the reset factory settings")

        case 7:
            print("This is the Call divert option")

        case 8:
            show("""\
                Welicome to Music
                1. Music player
                2. Radio
                3. Recorder
                4. Track list

                Please input the number to access that Music options:
                """)

            option8 = int(input())

            match option8:
                case 1:
                    show("""\
                        Welicome to Music player
                        There's nothing to do here sorry
                        """)
                case 2: print("This is the Radio option")
                case 3: print("Welicome to Incoming Recorder")
                case 4: print("This is Track list option")

        case 9: print("You are in Games Option")

        case 10: print("Welicome to calculator")

        case 11: print("Welicome to Reminders option")

        case 12:
            show("""\
                Welcome to Clock
                1. Alarm clock
                2. Clock settings
                3. Date setting
                4. Stopwatch
                5. Countdown timer
                6. Auto update of date and time

                Please input the corresponding number to access that Clock options:
                """)

            option122 = int(input())

            match option122:
                case 1: print("Welcome to Alarm clock")
                case 2: print("Welcome to Clock settings")
                case 3: print("Welcome to Date setting")
                case 4: print("Welcome to Stopwatch")
                case 5: print("Welcome to Countdown timer")
                case 6: print("Welcome to Auto update of date and time")

        case 13: print("You are currently in Profiles option")

        case 14: print("Welicome to Services")

        case 15: print("You are currently in SIM services option")

        case _: print("That menu isn't available yet")


if __name__ == "__main__":
    main()