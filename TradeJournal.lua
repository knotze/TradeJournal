local function avgrr(arr) 
	local Average = 0 
	local Total = 0 
	for i, rr in ipairs(arr) do 
		Total = Total + rr 
		Average = Total / #arr 

	end
	return Average
end	

local function winrate(arr)
    local trades = 0
    local losses = 0
    local wins = 0

    for i, trade in ipairs(arr) do
        trades = trades + 1
        if trade == "win" then
            wins = wins + 1
        else
            losses = losses + 1
        end
    end
	if trades == 0 then
        return 0 
    end
	local rate = (wins / trades) * 100 .. "%"
    return rate
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

    if win_count == 0 then
        return 0 
    end

    return total_win / win_count
end


local function average_loss(arr)
    local total_loss = 0
    local loss_count = 0
	for _, trade in ipairs(trades) do
        if trade < 0 then
            total_loss = total_loss + math.abs(trade)
            loss_count = loss_count + 1
        end
    end
    if loss_count == 0 then
        return 0 
    end

    return total_loss / loss_count
end

local lossrate = 1 - winrate()

local expectedValue = (winrate() * average_win()) - (lossrate() * average_loss())


















