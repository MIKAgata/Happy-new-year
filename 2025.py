import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_digit_art(digit, style=0):
    digits = {
        '0': [
            "   █████████   ",
            " ██         ██ ",
            "██           ██",
            "██           ██",
            "██           ██",
            "██           ██",
            "██           ██",
            "██           ██",
            "██           ██",
            "██           ██",
            "██           ██",
            " ██         ██ ",
            "   █████████   "
        ],
        '1': [
            "      ███      ",
            "    ██████     ",
            "      ███      ",
            "      ███      ",
            "      ███      ",
            "      ███      ",
            "      ███      ",
            "      ███      ",
            "      ███      ",
            "      ███      ",
            "      ███      ",
            "      ███      ",
            "   █████████   "
        ],
        '2': [
            "  ██████████   ",
            "██          ██ ",
            "██          ██ ",
            "           ██  ",
            "          ██   ",
            "        ██     ",
            "      ██       ",
            "    ██         ",
            "  ██           ",
            "██             ",
            "██             ",
            "██             ",
            "██████████████ "
        ],
        '3': [
            "  ██████████   ",
            "██          ██ ",
            "██          ██ ",
            "           ██  ",
            "          ██   ",
            "   ███████     ",
            "          ██   ",
            "           ██  ",
            "            ██ ",
            "██          ██ ",
            "██          ██ ",
            "██          ██ ",
            "  ██████████   "
        ],
        '4': [
            "██         ██  ",
            "██         ██  ",
            "██         ██  ",
            "██         ██  ",
            "██         ██  ",
            "██         ██  ",
            "██████████████ ",
            "██████████████ ",
            "          ██   ",
            "          ██   ",
            "          ██   ",
            "          ██   ",
            "          ██   "
        ],
        '5': [
            "██████████████ ",
            "██████████████ ",
            "██             ",
            "██             ",
            "██             ",
            "███████████    ",
            "           ██  ",
            "            ██ ",
            "            ██ ",
            "            ██ ",
            "██          ██ ",
            "██          ██ ",
            "  ██████████   "
        ],
        '6': [
            "   █████████   ",
            " ██        ██  ",
            "██          ██ ",
            "██             ",
            "██             ",
            "███████████    ",
            "██        ██   ",
            "██         ██  ",
            "██         ██  ",
            "██         ██  ",
            "██         ██  ",
            " ██       ██   ",
            "   ████████    "
        ],
        '7': [
            "██████████████ ",
            "██████████████ ",
            "            ██ ",
            "           ██  ",
            "          ██   ",
            "         ██    ",
            "        ██     ",
            "       ██      ",
            "      ██       ",
            "     ██        ",
            "    ██         ",
            "   ██          ",
            "  ██           "
        ],
        '8': [
            "   █████████   ",
            " ██        ██  ",
            "██          ██ ",
            "██          ██ ",
            "██          ██ ",
            " ██        ██  ",
            "   █████████   ",
            " ██        ██  ",
            "██          ██ ",
            "██          ██ ",
            "██          ██ ",
            " ██        ██  ",
            "   █████████   "
        ],
        '9': [
            "   █████████   ",
            " ██        ██  ",
            "██          ██ ",
            "██          ██ ",
            "██          ██ ",
            " ██        ██  ",
            "   ██████████  ",
            "           ██  ",
            "           ██  ",
            "           ██  ",
            "██         ██  ",
            " ██       ██   ",
            "   ████████    "
        ]
    }
    
    art = digits.get(str(digit), digits['0'])
    
   
    if style == 1:  
        art = [line.replace('█', '▓').replace('▓', '▒').replace(' ', '░') for line in art]
    elif style == 2:  
        art = [line.replace('█', '@').replace(' ', '#') for line in art]
    elif style == 3:  
        art = [line.replace('█', '█').replace(' ', '▓') for line in art]
    
    return art

def combine_digits(digits_str, style=0, spacing=2):
    digit_arts = [create_digit_art(d, style) for d in digits_str]
    
    combined = []
    for i in range(13):  
        row = (' ' * spacing).join(art[i] for art in digit_arts)
        combined.append(row)
    
    return combined

def get_terminal_size():
    try:
        size = os.get_terminal_size()
        return size.lines, size.columns
    except:
        return 25, 80 

def center_art(art_lines):
    terminal_lines, terminal_columns = get_terminal_size()
    
    if not art_lines:
        return art_lines
    
    max_length = max(len(line) for line in art_lines)
    left_padding = max(0, (terminal_columns - max_length) // 2)
    
    centered = [' ' * left_padding + line for line in art_lines]
    
    return centered

def create_frame(text, style=0, sparkle=False):
    art = combine_digits(text, style, spacing=2)
    centered = center_art(art)
    
    if sparkle:
        sparkled = []
        for line in centered:
            new_line = list(line)
            for i in range(len(new_line)):
                if random.random() < 0.01 and new_line[i] not in [' ', '░']:
                    new_line[i] = random.choice(['*', '·', '+', '°'])
            sparkled.append(''.join(new_line))
        centered = sparkled
    
    return centered

def display_frame(frame, title="", delay=0):
    clear_screen()
    
    terminal_lines, _ = get_terminal_size()
    
    art_height = len(frame)
    top_padding = max(0, (terminal_lines - art_height - 5) // 2)
    
    if title:
        print("\n" * (top_padding // 2))
        print(" " * 5 + "═" * 50)
        print(" " * 5 + f"    {title}")
        print(" " * 5 + "═" * 50 + "\n")
    
    # Tampilkan art
    for line in frame:
        print(line)
    
    if delay > 0:
        time.sleep(delay)

def sliding_effect(from_text, to_text, steps=25):
    frames = []
    
    for step in range(steps + 1):
        progress = step / steps
        
        
        frame = []
        for row in range(13):
            from_art = combine_digits(from_text, 0, 2)
            to_art = combine_digits(to_text, min(2, step // 5), 2)
            
            
            combined_row = ""
            from_row = from_art[row]
            to_row = to_art[row]
            
        
            offset = int((1 - progress) * len(from_row))
            
            
            for i in range(len(from_row)):
                if i < offset:
                    combined_row += from_row[i]
                else:
                    combined_row += to_row[i]
            
            frame.append(combined_row)
        
        centered = center_art(frame)
        frames.append(centered)
    
    return frames

def pixel_transition(from_text, to_text, steps=40):
    from_art = combine_digits(from_text, 0, 2)
    to_art = combine_digits(to_text, 2, 2)
    
    frames = []
    height = len(from_art)
    width = len(from_art[0])
    
    change_mask = []
    for y in range(height):
        row_mask = []
        for x in range(width):
            if x < len(from_art[y]) and x < len(to_art[y]):
                row_mask.append(from_art[y][x] != to_art[y][x])
            else:
                row_mask.append(False)
        change_mask.append(row_mask)
    
    total_changes = sum(sum(row) for row in change_mask)
    changes_per_step = max(1, total_changes // steps)
    
    current_art = [list(row) for row in from_art]
    
    for step in range(steps):
        changes_made = 0
        while changes_made < changes_per_step:
            y = random.randint(0, height - 1)
            x = random.randint(0, width - 1)
            
            if y < len(change_mask) and x < len(change_mask[y]) and change_mask[y][x]:
                current_art[y][x] = to_art[y][x]
                change_mask[y][x] = False
                changes_made += 1
        

        frame = [''.join(row) for row in current_art]
        centered = center_art(frame)
        frames.append(centered)
    
    final_frame = center_art(to_art)
    frames.append(final_frame)
    
    return frames

def number_transform_effect():
    frames = []
    
    for i in range(3):
        frame = create_frame("2025", 0, sparkle=(i%2==0))
        frames.append(frame)
    
    for i in range(5):
        frame = create_frame("2025", 1, sparkle=True)
        frames.append(frame)
    
    transform_stages = [
        "2025", "2025", "2025", 
        "202▢", "202▣", "202▩",
        "2026", "2026", "2026"
    ]
    
    for stage in transform_stages:
        if "▢" in stage or "▣" in stage or "▩" in stage:
            art_202 = combine_digits("202", 2, 2)
            custom_char = [
                "    █████    ",
                "  ██     ██  ",
                " ██       ██ ",
                "██         ██",
                "██    ██   ██",
                "██   ███   ██",
                "██  █████  ██",
                "██ ██   ██ ██",
                "████     ████",
                "███       ███",
                " ██       ██ ",
                "  ██     ██  ",
                "    █████    "
            ] if "▩" in stage else [
                "            ",
                "    ████    ",
                "  ██  ██    ",
                " ██   ██    ",
                "██    ██    ",
                "██    ██    ",
                "██    ██    ",
                "██    ██    ",
                "██    ██    ",
                "██    ██    ",
                " ██   ██    ",
                "  ██  ██    ",
                "    ████    "
            ] if "▣" in stage else [
                "            ",
                "            ",
                "    ████    ",
                "  ██  ██    ",
                " ██   ██    ",
                "██    ██    ",
                "██    ██    ",
                "██    ██    ",
                "██    ██    ",
                "██    ██    ",
                " ██   ██    ",
                "  ██  ██    ",
                "    ████    "
            ]
            
            combined = []
            for i in range(13):
                combined.append(art_202[i] + "  " + custom_char[i])
            
            centered = center_art(combined)
            frames.append(centered)
        else:
            frame = create_frame(stage, 2, sparkle=("6" in stage))
            frames.append(frame)
    
    for i in range(8):
        style = 3 if i > 4 else 2
        frame = create_frame("2026", style, sparkle=True)
        frames.append(frame)
    
    return frames

def countdown_sequence():
    countdown_frames = []
    
    for i in range(3, 0, -1):
        for _ in range(2):
            frame = create_frame(str(i), 2, sparkle=True)
            centered = center_art(frame)
            
            terminal_lines, terminal_columns = get_terminal_size()
            padding_top = (terminal_lines - 13) // 2
            
            final_frame = []
            final_frame.append("\n" * (padding_top - 2))
            final_frame.append(" " * ((terminal_columns - 40) // 2) + "╔══════════════════════════════════════╗")
            final_frame.append(" " * ((terminal_columns - 40) // 2) + "║         TRANSISI DIMULAI DALAM       ║")
            final_frame.extend(centered)
            final_frame.append(" " * ((terminal_columns - 40) // 2) + "╚══════════════════════════════════════╝")
            
            countdown_frames.append(final_frame)
    
    return countdown_frames

def final_celebration():
    celebration_frames = []
    
    messages = [
        "SELAMAT TAHUN BARU 2026!",
        "2025 → 2026",
        "WELCOME 2026!",
        "NEW BEGINNINGS!",
        "HAPPY NEW YEAR!"
    ]
    
    for i in range(20):
        art = combine_digits("2026", 3, 2)
        centered = center_art(art)
        
        if i % 3 == 0:
            centered = [line.replace('█', '@').replace('▓', '#') for line in centered]
        elif i % 3 == 1:
            centered = [line.replace('█', '█').replace('▓', '░') for line in centered]
        
        terminal_lines, terminal_columns = get_terminal_size()
        message = messages[(i // 4) % len(messages)]
        
        final_frame = []
        final_frame.append("\n" * 2)
        final_frame.append(" " * ((terminal_columns - len(message)) // 2) + "★ " + message + " ★")
        final_frame.append(" " * ((terminal_columns - len(message)) // 2) + "═" * (len(message) + 4))
        final_frame.append("")
        final_frame.extend(centered)
        final_frame.append("")
        final_frame.append(" " * ((terminal_columns - 30) // 2) + "* " + "・".join(["★"] * 10) + " *")
        
        celebration_frames.append(final_frame)
    
    return celebration_frames

def main():
    
    print("Menyiapkan animasi pergantian tahun 2025 → 2026...")
    time.sleep(1.5)
    
    try:
        print("\n" * 3)
        for i in range(5):
            frame = create_frame("2025", 0, sparkle=(i%3==0))
            display_frame(frame, "TAHUN 2025", 0.3)
        

        print("\n" * 3)
        countdown_frames = countdown_sequence()
        for frame in countdown_frames:
            clear_screen()
            for line in frame:
                print(line)
            time.sleep(0.8)
        
        time.sleep(0.5)
        

        print("\n" * 3)
        transform_frames = number_transform_effect()
        for i, frame in enumerate(transform_frames):
            display_frame(frame, "TRANSFORMASI", 0.1)
        
        time.sleep(0.5)
        
     
        print("\n" * 3)
        sliding_frames = sliding_effect("2025", "2026", 30)
        for frame in sliding_frames:
            display_frame(frame, "SLIDING TRANSISI", 0.05)
        
        time.sleep(0.5)
        
 
        print("\n" * 3)
        pixel_frames = pixel_transition("2025", "2026", 25)
        for frame in pixel_frames:
            display_frame(frame, "PIXEL TRANSITION", 0.08)
        
        time.sleep(0.5)
        

        print("\n" * 3)
        celebration_frames = final_celebration()
        for frame in celebration_frames:
            clear_screen()
            for line in frame:
                print(line)
            time.sleep(0.15)
        
  
        clear_screen()
        terminal_lines, terminal_columns = get_terminal_size()
        
        print("\n" * (terminal_lines // 4))
        
  
        border = "╔" + "═" * (terminal_columns - 2) + "╗"
        print(border)
        
  
        final_art = combine_digits("2026", 3, 3)
        centered_final = center_art(final_art)
        
        for line in centered_final:
            print(line)
        
  
        print("\n" * 2)
        message = "SELAMAT TAHUN BARU 2026!"
        print(" " * ((terminal_columns - len(message)) // 2) + message)
        print(" " * ((terminal_columns - 50) // 2) + "semoga anda baik baik saja!")
        

        print("\n" * (terminal_lines // 4 - 5))
        print("╚" + "═" * (terminal_columns - 2) + "╝")
        
    
        time.sleep(5)
        
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\nTerjadi error: {e}")

def show_welcome():
  
    clear_screen()
    terminal_lines, terminal_columns = get_terminal_size()
    
    print("\n" * (terminal_lines // 4))
    
    welcome_text = [
        "╔══════════════════════════════════════════════════════════╗",
        "║                                                          ║",
        "║                   PERGANTIAN TAHUN 2025 → 2026           ║",
        "║                                                          ║",
        "║                    ASCII ART EDITION                     ║",
        "║                                                          ║",
        "║              Tekan Enter untuk memulai...                ║",
        "║                                                          ║",
        "╚══════════════════════════════════════════════════════════╝"
    ]
    
    for line in welcome_text:
        padding = (terminal_columns - len(line)) // 2
        print(" " * padding + line)
    
    print("\n" * (terminal_lines // 4))
    
    input()
    main()

if __name__ == "__main__":
    show_welcome()
