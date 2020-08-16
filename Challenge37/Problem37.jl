function MainFunction()
    PrimeNumber = []
    TruncablePrimeNumber = []
    i = 2
    while length(TruncablePrimeNumber) < 11
        if IsPrime(i)
            push!(PrimeNumber, i)
            @show i
            if IsTruncable(i, PrimeNumber) && InverseIsTruncable(i, PrimeNumber) && i > 10
                push!(TruncablePrimeNumber, i)
                @show TruncablePrimeNumber
            end
        end
        i = i+1
    end
    println(sum(TruncablePrimeNumber))
end
function IsPrime(number)
    if number == 2
        return true
    end
    if number % 2 == 0
        return false
    end
    boundary = floor(sqrt(number))
    for i in 3:2:boundary
        if number % i == 0
            return false
        end
    end
    return true
end

function IsTruncable(number, PrimeList)
    if number ∉ PrimeList
        return false
    end
    if length(string(number)) == 1
        return number in PrimeList
    else
        SNumber = split(string(number), "")
        return IsTruncable(parse(Int, join(deleteat!(SNumber, 1))), PrimeList)
    end
end
function InverseIsTruncable(number, PrimeList)
    if number ∉ PrimeList
        return false
    end
    if length(string(number)) == 1
        return number in PrimeList
    else
        SNumber = split(string(number), "")
        return InverseIsTruncable(parse(Int, join(deleteat!(SNumber, length(SNumber)))), PrimeList)
    end
end
MainFunction()
