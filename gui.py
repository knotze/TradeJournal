


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, Label
import re


OUTPUT_PATH = Path(__file__).parent


window = Tk()

window.geometry("1000x550")
window.configure(bg = "#4A5898")


canvas = Canvas(
    window,
    bg = "#4A5898",
    height = 550,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# List to store buttons for easy show/hide
menu_buttons = []
canvas.create_rectangle(
    0.0,
    0.0,
    1000.0,
    82.9,
    fill="#000000",
    outline="")

canvas.create_text(
    41.1,
    21.7,
    anchor="nw",
    text="EzJournal",
    fill="#FFFFFF",
    font=("Inter SemiBold", 42 * -1)
)


def show_dashboard_view():
    """Show the main menu with buttons"""
    button_1.place(x=35.6, y=133.1, width=257.2, height=82.9)
    button_2.place(x=646.8, y=133.1, width=246.0, height=82.9)
    button_3.place(x=351.4, y=133.1, width=205.7, height=87.4)
    # hide journal widgets if visible
    try:
        label_result.place_forget()
        entry_result.place_forget()
        label_rr.place_forget()
        entry_rr.place_forget()
        label_prof.place_forget()
        entry_prof.place_forget()
        log_button.place_forget()
    except NameError:
        pass
    back_button.place_forget()

    # hide dashboard stats
    try:
        canvas.itemconfig(stat_box1, state='hidden')
        canvas.itemconfig(stat_box2, state='hidden')
        canvas.itemconfig(stat_box3, state='hidden')
        canvas.itemconfig(stat_box4, state='hidden')
        canvas.itemconfig(stat_box5, state='hidden')
        stat_winrate.place_forget()
        stat_winrate_val.place_forget()
        stat_avgrr.place_forget()
        stat_avgrr_val.place_forget()
        stat_avgwin.place_forget()
        stat_avgwin_val.place_forget()
        stat_avgloss.place_forget()
        stat_avgloss_val.place_forget()
        stat_ev.place_forget()
        stat_ev_val.place_forget()
    except NameError:
        pass


def show_main_window():
    """Show the main window without buttons"""
    button_1.place_forget()
    button_2.place_forget()
    button_3.place_forget()
    # hide journal widgets
    try:
        label_result.place_forget()
        entry_result.place_forget()
        label_rr.place_forget()
        entry_rr.place_forget()
        label_prof.place_forget()
        entry_prof.place_forget()
        log_button.place_forget()
    except NameError:
        pass
    back_button.place(x=35.6, y=470, width=100, height=50)
    # update and show dashboard stats
    try:
        wins, rrs, profs = read_trade_data()
        winrate_v, avgrr_v, avgwin_v, avgloss_v, ev_v = compute_metrics(wins, rrs, profs)
    except Exception:
        winrate_v = avgrr_v = avgwin_v = avgloss_v = ev_v = 0

    # place and set values
    canvas.itemconfig(stat_box1, state='normal')
    stat_winrate.place(x=85, y=160)
    stat_winrate_val.config(text=f"{winrate_v*100:.1f}%")
    stat_winrate_val.place(x=95, y=195)

    canvas.itemconfig(stat_box2, state='normal')
    stat_avgwin.place(x=295, y=160)
    stat_avgwin_val.config(text=f"{avgwin_v:.2f}")
    stat_avgwin_val.place(x=305, y=195)

    canvas.itemconfig(stat_box3, state='normal')
    stat_avgloss.place(x=505, y=160)
    stat_avgloss_val.config(text=f"{avgloss_v:.2f}")
    stat_avgloss_val.place(x=515, y=195)

    canvas.itemconfig(stat_box4, state='normal')
    stat_avgrr.place(x=715, y=160)
    stat_avgrr_val.config(text=f"{avgrr_v:.2f}")
    stat_avgrr_val.place(x=725, y=195)

    canvas.itemconfig(stat_box5, state='normal')
    stat_ev.place(x=375, y=295)
    stat_ev_val.config(text=f"{ev_v:.2f}")
    stat_ev_val.place(x=420, y=330)

button_1 = Button(
    text="Dashboard",
    font=("Inter SemiBold", 28),
    fg="#FFFFFF",
    bg="#2E3B7F",
    borderwidth=0,
    highlightthickness=0,
    highlightcolor="#2E3B7F",
    activebackground="#1A1F4D",
    activeforeground="#FFFFFF",
    command=show_main_window,
    relief="flat"
)
button_1.place(
    x=35.6,
    y=133.1,
    width=257.2,
    height=82.9
)
menu_buttons.append(button_1)

button_2 = Button(
    text="Journal",
    font=("Inter SemiBold", 28),
    fg="#FFFFFF",
    bg="#2E3B7F",
    borderwidth=0,
    highlightthickness=0,
    highlightcolor="#2E3B7F",
    activebackground="#1A1F4D",
    activeforeground="#FFFFFF",
    command=lambda: show_journal_view(),
    relief="flat"
)
button_2.place(
    x=646.8,
    y=133.1,
    width=246.0,
    height=82.9
)
menu_buttons.append(button_2)

button_3 = Button(
    text="Calendar",
    font=("Inter SemiBold", 24),
    fg="#FFFFFF",
    bg="#2E3B7F",
    borderwidth=0,
    highlightthickness=0,
    highlightcolor="#2E3B7F",
    activebackground="#1A1F4D",
    activeforeground="#FFFFFF",
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=351.4,
    y=133.1,
    width=205.7,
    height=87.4
)
menu_buttons.append(button_3)

# --- Journal view widgets (created but not placed) ---
label_result = Label(window, text="Result (win/loss):", fg="#FFFFFF", bg="#4A5898", font=("Inter SemiBold", 14))
entry_result = Entry(window, font=("Inter SemiBold", 14), fg="#FFFFFF", bg="#2E3B7F", relief="flat", bd=2)
entry_result.insert(0, "")

label_rr = Label(window, text="Risk:Reward:", fg="#FFFFFF", bg="#4A5898", font=("Inter SemiBold", 14))
entry_rr = Entry(window, font=("Inter SemiBold", 14), fg="#FFFFFF", bg="#2E3B7F", relief="flat", bd=2)
entry_rr.insert(0, "")

label_prof = Label(window, text="Profit / Loss:", fg="#FFFFFF", bg="#4A5898", font=("Inter SemiBold", 14))
entry_prof = Entry(window, font=("Inter SemiBold", 14), fg="#FFFFFF", bg="#2E3B7F", relief="flat", bd=2)
entry_prof.insert(0, "")

def log_trade():
    # read values
    res = entry_result.get().strip().lower()
    if res.startswith('w'):
        res_val = "win"
    else:
        res_val = "loss"
    try:
        rr_val = float(entry_rr.get())
    except Exception:
        rr_val = 0
    try:
        prof_val = float(entry_prof.get())
    except Exception:
        prof_val = 0
    # append to TradeJournal.lua
    try:
        lua_file = OUTPUT_PATH / "TradeJournal.lua"
        with open(lua_file, "a", encoding="utf-8") as f:
            f.write("\n-- Logged from GUI\n")
            f.write(f'table.insert(winsLosses, "{res_val}")\n')
            f.write(f"table.insert(rr, {rr_val})\n")
            f.write(f"table.insert(profLoss, {prof_val})\n")
    except Exception as e:
        print("Failed to write to TradeJournal.lua:", e)
    # clear inputs (safely)
    try:
        entry_result.delete(0, 'end')
    except Exception:
        pass
    try:
        entry_rr.delete(0, 'end')
    except Exception:
        pass
    try:
        entry_prof.delete(0, 'end')
    except Exception:
        pass

log_button = Button(
    text="Log Trade",
    font=("Inter SemiBold", 16),
    fg="#FFFFFF",
    bg="#2E3B7F",
    borderwidth=0,
    highlightthickness=0,
    command=log_trade,
    relief="flat",
    activebackground="#1A1F4D",
    activeforeground="#FFFFFF"
)

def show_journal_view():
    # hide main menu buttons
    button_1.place_forget()
    button_2.place_forget()
    button_3.place_forget()
    # hide stat cards
    try:
        canvas.itemconfig(stat_box1, state='hidden')
        canvas.itemconfig(stat_box2, state='hidden')
        canvas.itemconfig(stat_box3, state='hidden')
        canvas.itemconfig(stat_box4, state='hidden')
        canvas.itemconfig(stat_box5, state='hidden')
    except NameError:
        pass
    # place journal fields with modern styling
    label_result.place(x=150, y=160)
    entry_result.place(x=150, y=190, width=700, height=40)
    label_rr.place(x=150, y=250)
    entry_rr.place(x=150, y=280, width=700, height=40)
    label_prof.place(x=150, y=340)
    entry_prof.place(x=150, y=370, width=700, height=40)
    log_button.place(x=425, y=430, width=150, height=45)
    back_button.place(x=35.6, y=470, width=100, height=50)


# --- Dashboard stats widgets (cards with canvas backgrounds) ---
stat_box1 = canvas.create_rectangle(80, 150, 260, 240, fill="#2E3B7F", outline="#1A1F4D", width=2)
stat_winrate = Label(window, text="Winrate", fg="#B0B8E0", bg="#2E3B7F", font=("Inter", 11))
stat_winrate_val = Label(window, text="0%", fg="#FFFFFF", bg="#2E3B7F", font=("Inter SemiBold", 20))

stat_box2 = canvas.create_rectangle(290, 150, 470, 240, fill="#2E3B7F", outline="#1A1F4D", width=2)
stat_avgwin = Label(window, text="Average Win", fg="#B0B8E0", bg="#2E3B7F", font=("Inter", 11))
stat_avgwin_val = Label(window, text="0.00", fg="#FFFFFF", bg="#2E3B7F", font=("Inter SemiBold", 20))

stat_box3 = canvas.create_rectangle(500, 150, 680, 240, fill="#2E3B7F", outline="#1A1F4D", width=2)
stat_avgloss = Label(window, text="Average Loss", fg="#B0B8E0", bg="#2E3B7F", font=("Inter", 11))
stat_avgloss_val = Label(window, text="0.00", fg="#FFFFFF", bg="#2E3B7F", font=("Inter SemiBold", 20))

stat_box4 = canvas.create_rectangle(710, 150, 890, 240, fill="#2E3B7F", outline="#1A1F4D", width=2)
stat_avgrr = Label(window, text="Average RR", fg="#B0B8E0", bg="#2E3B7F", font=("Inter", 11))
stat_avgrr_val = Label(window, text="0.00", fg="#FFFFFF", bg="#2E3B7F", font=("Inter SemiBold", 20))

stat_box5 = canvas.create_rectangle(350, 280, 650, 370, fill="#2E3B7F", outline="#1A1F4D", width=2)
stat_ev = Label(window, text="Expected Value", fg="#B0B8E0", bg="#2E3B7F", font=("Inter", 11))
stat_ev_val = Label(window, text="0.00", fg="#FFFFFF", bg="#2E3B7F", font=("Inter SemiBold", 20))

# Hide all stat boxes on startup
canvas.itemconfig(stat_box1, state='hidden')
canvas.itemconfig(stat_box2, state='hidden')
canvas.itemconfig(stat_box3, state='hidden')
canvas.itemconfig(stat_box4, state='hidden')
canvas.itemconfig(stat_box5, state='hidden')


def read_trade_data():
    """Parse TradeJournal.lua for table.insert lines and reconstruct arrays."""
    wins = []
    rrs = []
    profs = []
    try:
        lua_file = OUTPUT_PATH / "TradeJournal.lua"
        with open(lua_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # winsLosses inserts
                m = re.match(r'table\.insert\(winsLosses,\s*"(win|loss)"\)', line)
                if m:
                    wins.append(m.group(1))
                    continue
                # rr inserts
                m = re.match(r'table\.insert\(rr,\s*([0-9+\-\.eE]+)\)', line)
                if m:
                    try:
                        rrs.append(float(m.group(1)))
                    except Exception:
                        pass
                    continue
                # profLoss inserts
                m = re.match(r'table\.insert\(profLoss,\s*([0-9+\-\.eE]+)\)', line)
                if m:
                    try:
                        profs.append(float(m.group(1)))
                    except Exception:
                        pass
                    continue
    except FileNotFoundError:
        pass
    return wins, rrs, profs


def compute_metrics(wins, rrs, profs):
    # winrate
    trades = len(wins)
    winrate_v = (sum(1 for w in wins if w == 'win') / trades) if trades > 0 else 0
    # average rr
    avgrr_v = (sum(rrs) / len(rrs)) if len(rrs) > 0 else 0
    # average win
    wins_list = [p for p in profs if p > 0]
    avgwin_v = (sum(wins_list) / len(wins_list)) if len(wins_list) > 0 else 0
    # average loss (as positive number)
    loss_list = [abs(p) for p in profs if p < 0]
    avgloss_v = (sum(loss_list) / len(loss_list)) if len(loss_list) > 0 else 0
    # expected value
    lossrate = 1 - winrate_v
    ev_v = (winrate_v * avgwin_v) - (lossrate * avgloss_v)
    return winrate_v, avgrr_v, avgwin_v, avgloss_v, ev_v


back_button = Button(
    text="Back",
    font=("Inter SemiBold", 16),
    fg="#FFFFFF",
    bg="#2E3B7F",
    borderwidth=0,
    highlightthickness=0,
    highlightcolor="#2E3B7F",
    activebackground="#1A1F4D",
    activeforeground="#FFFFFF",
    command=show_dashboard_view,
    relief="flat"
)


window.resizable(False, False)
window.mainloop()
