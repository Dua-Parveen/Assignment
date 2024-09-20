# Trafic light signal Rules:

def rule (light):
    match light:
        case "red":
            return "STOP"
        case "Red":
            return "STOP"
        case "RED":
            return "STOP"
        case "orange":
            return "READY"
        case "Orange":
            return "READY"
        case "ORANGE":
            return "READY"
        case "green":
            return"GO"
        case "Green":
            return"GO"
        case "GREEN":
            return"GO"

print(rule(str(input("Enter your colour from \"red\", \"orange\", \"green\""))))
