print("Welcome to the menu options \nList of menu options are\n1.Phone book\n2.Messages\n3.Chat\n4.Call register\n5.tones\n6.settings\n7.Call divert\n8.Music\n9.Games\n10.Calculator\n11.Reminders\n12.Clock\n13.Profiles\n14.Services\n15.Sim services\n")

option = int(input("Enter the corresponding number  access that menu options: "))

match option:

    case 1:
        print("Welcome to phone book\n1. Search\n2. Service Nos. 1\n3. Add name\n4. Erase\n5. Edit\n6. Copy\n7. Assign tone\n8. Send b' card\n9. Options\n10. Speed dials\n11. Voice tags\n")

        option = int(input("Enter the corresponding number to access that menu options: "))

        match option:

            case 1: print("Welcome to search\nThere's nothing to do here sorry")

            case 2: print("Welcome to service Nos1\nThere's nothing to do here sorry")

            case 3: print("Welcome to Add name\nThere's nothing to do here sorry")

            case 4: print("Welcome to Erase\nThere's nothing to do here sorry")
            
            case 5: print("Welcome to Edit\nThere's nothing to do here sorry")
            
            case 6: print("Welcome to Copy\nThere's nothing to do here sorry")
            
            case 7: print("Welcome to Assign tone\nThere's nothing to do here sorry")
            
            case 8: print("Welcome to Send b'card\nThere's nothing to do here sorry")
            
            case 9:
                
                print("Welcome to Options\n1. Memory in use\n2. Type of view\n3. Memory status\n")
                
                option = int(input("Enter the corresponding number to access that menu options:"))
                
                
                match option:
                    
                    case 1: print("Welcome to Memory in use\nThere's nothing to do here sorry")
                    
                    case 2: print("Welcome to Type of view\nThere's nothing to do here sorry")
                    
                    case 3: print("Welcome to memory status\nThere's nothing to do here sorry")
                    
            case 10: print("Welcome to Speed dials\nThere's nothing to do here sorry")
            
            case 11: print("Welcome to voice tags\nThere's nothing to do here sorry")

    case 2:
        
        print("Welcome to Messages\n1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages\n5. Templates\n6. Smileys\n7. Message settings\n8. Info service\n9. Voice mailbox number 4\n10. Service command editor\n")
        
        option = int(input("Enter the corresponding number to access that message option:"))
        
        match option:
            case 1: print("Welcome to Write messages\nThere's nothing to do here sorry")
            
            case 2: print("Welcome to Inbox\nThere's nothing to do here sorry")
            
            case 3: print("Welcome to Outbox\nThere's nothing to do here sorry")
            
            case 4: print("Welcome to Picture messages\nThere's nothing to do here sorry")
            
            case 5: print("Welcome to Templates\nThere's nothing to do here sorry")
            case 6: print("Welcome to Smileys\nThere's nothing to do here sorry")
            case 7:
                print("Welcome to Message settings\n1. Set 12\n2. Common 3\n")
                option = int(input("Enter the corresponding number to access that message option:"))
                
                match option:
                    case 1:
                        print("Welcome to Set 12\n1. Message centre number\n2. Messages sent as\n3. Message validity\n")
                        option = int(input("Enter the corresponding number to access that Set12 option:"))
                        
                        match option:
                            case 1: print("Welcome to centre number\nThere's nothing to do here sorry")
                            case 2: print("Welcome to Messages sent as\nThere's nothing to do here sorry")
                            case 3: print("Welcome to Message validity\nThere's nothing to do here sorry")
                    case 2:
                        print("Welcome to Common 3\n1. Delivery reports\n2. Reply via same centre\n3. Character support\n")
                        option = int(input("Enter the corresponding number to access that Common 3 option:"))
                      
                        match option:
                            case 1: print("Welcome to Delivery reports\nThere's nothing to do here sorry")
                            case 2: print("Welcome to Reply via same centre\nThere's nothing to do here sorry")
                            case 3: print("Welcome to Character support\nThere's nothing to do here sorry")
            case 8: print("Welcome to info service\nThere's nothing to do here sorry")
            case 9: print("Welcome to Voice mailbox number 4\nThere's nothing to do here sorry")
            case 10: print("Welcome to Service command editor\nThere's nothing to do here sorry")

    case 3: print("Welcome to Chat\nThere's nothing to do here sorry")

    case 4:
        print("Welcome to Call register\n1. Missed calls\n2. Received calls\n3. Dialled numbers\n4. Erase recent call lists\n5. Show call duration\n6. Show call costs\n7. Call cost settings\n8. Prepaid credit\n")
        option = int(input("Enter the corresponding number to access that Call register option: "))
        
        match option:
            case 1: print("Welcome to Missed calls\nThere's nothing to do here sorry")
            case 2: print("Welcome to Received calls\nThere's nothing to do here sorry")
            case 3: print("Welcome to Dialled numbers\nThere's nothing to do here sorry")
            case 4: print("Welcome to Erase recent call lists\nThere's nothing to do here sorry")
            case 5:
                option = int(input("Welcome to Show call duration\n1. Last call duration\n2. All calls' duration\n3. Received calls' duration\n4. Dialled calls' duration\n5. Clear timers\n"))
                
                match option:
                    case 1: print("Welcome to Last call duration\nThere's nothing to do here sorry")
                    case 2: print("Welcome to All calls' duration\nThere's nothing to do here sorry")
                    case 3: print("Welcome to Received calls' duration\nThere's nothing to do here sorry")
                    case 4: print("Welcome to Dialled calls' duration\nThere's nothing to do here sorry")
                    case 5: print("Welcome to Clear timers\nThere's nothing to do here sorry")
            case 6:
                option = int(input("Welcome to Show call costs\n1. Last call cost\n2. All calls' cost\n3. Clear counters\n"))
                
                match option:
                    case 1: print("Welcome to Last call cost\nThere's nothing to do here sorry")
                    case 2: print("Welcome to All calls' cost\nThere's nothing to do here sorry")
                    case 3: print("Welcome to Clear counters\nThere's nothing to do here sorry")
            case 7:
                option = int(input("Welcome to Call cost settings\n1. Call cost limit\n2. Show costs in\n"))
                
                match option:
                    case 1: print("Welcome to Call cost limit\nThere's nothing to do here sorry")
                    case 2: print("Welcome to Show costs in\nThere's nothing to do here sorry")
            case 8: print("Welcome to Prepaid credit\nThere's nothing to do here sorry")

    case 5:
        print("Welcome to Tones\n1. Ringing tone\n2. Ringing volume\n3. Incoming call alert\n4. Message alert tone\n5. Keypad tones\n6. Warning tones\n7. Vibrating alert\n8. Screen saver\n")
        option = int(input("Enter the corresponding number to access that Tones options:"))
       
        match option:
            case 1: print("Welcome to Ringing tone\nThere's nothing to do here sorry")
            case 2: print("Welcome to Ringing volume\nThere's nothing to do here sorry")
            case 3: print("Welcome to Incoming call alert\nThere's nothing to do here sorry")
            case 4: print("Welcome to Message alert tone\nThere's nothing to do here sorry")
            case 5: print("Welcome to Keypad tones\nThere's nothing to do here sorry")
            case 6: print("Welcome to Warning tones\nThere's nothing to do here sorry")
            case 7: print("Welcome to Vibrating alert\nThere's nothing to do here sorry")
            case 8: print("Welcome to Screen saver\nThere's nothing to do here sorry")

    case 6:
        print("Welcome to Settings\n1. Call settings\n2. Phone settings\n3. Security settings\n4. Restore factory settings\n")
        option = int(input("Enter the corresponding number to access that Settings options:"))
        
        match option:
            case 1:
                print("Welcome to Call settings\n1. Automatic redial\n2. Speed dialling\n3. Call waiting options\n4. Own number sending\n5. Phone line in use\n6. Automatic answer\n")
                option = int(input("Enter the corresponding number to access that Call settings options:"))
               
                match option:
                    case 1: print("Welcome to Automatic redial\nThere's nothing to do here sorry")
                    case 2: print("Welcome to Speed dialling\nThere's nothing to do here sorry")
                    case 3: print("Welcome to Call waiting options\nThere's nothing to do here sorry")
                    case 4: print("Welcome to Own number sending\nThere's nothing to do here sorry")
                    case 5: print("Welcome to Phone line in use\nThere's nothing to do here sorry")
                    case 6: print("Welcome to Automatic answer\nThere's nothing to do here sorry")
            case 2:
                print("Welcome to Phone settings\n1. Language\n2. Cell info display\n3. Welcome note\n4. Network selection\n5. Confirm SIM service actions\n")
                option = int(input("Enter the corresponding number to access that Phone settings options:"))
                
                match option:
                    case 1: print("Welcome to Language\nThere's nothing to do here sorry")
                    case 2: print("Welcome to Cell info display\nThere's nothing to do here sorry")
                    case 3: print("Welcome to Welcome note\nThere's nothing to do here sorry")
                    case 4: print("Welcome to Network selection\nThere's nothing to do here sorry")
                    case 5: print("Welcome to Confirm SIM service actions\nThere's nothing to do here sorry")
            case 3:
                print("Welcome to Security settings\n1. PIN code request\n2. Call barring service\n3. Fixed dialling\n4. Closed user group\n5. Security level\n6. Change access codes\n")
                option = int(input("Enter the corresponding number to access that Security settings option:"))
                
                match option:
                    case 1: print("Welcome to PIN code request\nThere's nothing to do here sorry")
                    case 2: print("Welcome to Call barring service\nThere's nothing to do here sorry")
                    case 3: print("Welcome to Fixed dialling\nThere's nothing to do here sorry")
                    case 4: print("Welcome to Closed user group\nThere's nothing to do here sorry")
                    case 5: print("Welcome to Security level\nThere's nothing to do here sorry")
                    case 6: print("Welcome to Change access codes\nThere's nothing to do here sorry")
            case 4: print("Welcome to Restore factory settings\nThere's nothing to do here sorry")

    case 7: print("Welcome to Call divert\nThere's nothing to do here sorry")

    case 8:
        print("Welcome to Music\n1. Music player\n2. Radio\n3. Recorder\n4. Track list\n")
        option = int(input("Enter the corresponding number to access that Music options:"))
      
        match option:
            case 1: print("Welcome to Music player\nThere's nothing to do here sorry")
            case 2: print("Welcome to Radio\nThere's nothing to do here sorry")
            case 3: print("Welcome to Recorder\nThere's nothing to do here sorry")
            case 4: print("Welcome to Track list\nThere's nothing to do here sorry")

    case 9: print("Welcome to Games\nThere's nothing to do here sorry")

    case 10: print("Welcome to Calculator\nThere's nothing to do here sorry")

    case 11: print("Welcome to Reminders\nThere's nothing to do here sorry")

    case 12:
        print("Welcome to Clock\n1. Alarm clock\n2. Clock settings\n3. Date setting\n4. Stopwatch\n5. Countdown timer\n6. Auto update of date and time\n")
       
        option = int(input("Enter the corresponding number to access that Clock options:"))
      
        match option:
            case 1: print("Welcome to Alarm clock\nThere's nothing to do here sorry")
            
            case 2: print("Welcome to Clock settings\nThere's nothing to do here sorry")
            
            case 3: print("Welcome to Date setting\nThere's nothing to do here sorry")
            
            case 4: print("Welcome to Stopwatch\nThere's nothing to do here sorry")
            
            case 5: print("Welcome to Countdown timer\nThere's nothing to do here sorry")
            
            case 6: print("Welcome to Auto update of date and time\nThere's nothing to do here sorry")

    case 13: print("Welcome to Profiles\nThere's nothing to do here sorry")

    case 14: print("Welcome to Services\nThere's nothing to do here sorry")

    case 15: print("Welcome to SIM services2\nThere's nothing to do here sorry")