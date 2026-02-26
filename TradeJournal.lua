print("Welcome to your personal trading journal")

local winsLosses = {} 
local rr = {} 
local profLoss = {} 

print("Would you like to log a trade? (yes/no)")
local l = io.read():lower()
if l == "yes" then
    print("Did you win this trade (yes/no)?")
    local wl = io.read():lower()
    if wl == "yes" then
        table.insert(winsLosses, "win")
    elseif wl == "no" then 
        table.insert(winsLosses, "loss")
    end

    print("What was your risk:reward on this trade (no colons)?")
    local RR = tonumber(io.read())
    table.insert(rr, RR)

    print("What was your profit or loss on this trade?")
    local PF = tonumber(io.read())
    table.insert(profLoss, PF)
end


local function avgrr(arr) 
    local Total = 0 
    for i, val in ipairs(arr) do 
        Total = Total + val 
    end
    if #arr == 0 then return 0 end
    return Total / #arr
end    


local function winrate(arr)
    local trades = #arr
    if trades == 0 then return 0 end

    local wins = 0
    for _, trade in ipairs(arr) do
        if trade == "win" then
            wins = wins + 1
        end
    end
    return wins / trades 
end


local function average_win(trades)
    local total_win = 0
    local win_count = 0

    for _, trade in ipairs(trades) do
        if trade > 0 then
            total_win = total_win + trade
            win_count = win_count + 1
        end
    end

    if win_count == 0 then return 0 end
    return total_win / win_count
end

local function average_loss(arr)
    local total_loss = 0
    local loss_count = 0
    for _, trade in ipairs(arr) do
        if trade < 0 then
            total_loss = total_loss + math.abs(trade)
            loss_count = loss_count + 1
        end
    end
    if loss_count == 0 then return 0 end
    return total_loss / loss_count
end


local numberWinRate = winrate(winsLosses)
local lossrate = 1 - numberWinRate
local expectedValue = (numberWinRate * average_win(profLoss)) - (lossrate * average_loss(profLoss))


print("Trading Summary")
print("Trades logged: " .. #winsLosses)
print("Win rate: " .. (numberWinRate * 100) .. "%")
print("Average RR: " .. avgrr(rr))
print("Average win: " .. average_win(profLoss))
print("Average loss: " .. average_loss(profLoss))
print("Expected value: " .. expectedValue)
