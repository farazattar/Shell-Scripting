using System;

class Program
{
    static void Main()
    {
        // Replace this value with your SINEC time
        uint sinecTime = 123456789;

        DateTime realDateTime = ConvertSinecToDateTime(sinecTime);

        Console.WriteLine("SINEC Time: " + sinecTime);
        Console.WriteLine("Real Date Time: " + realDateTime.ToString("yyyy-MM-dd HH:mm:ss"));
    }

    static DateTime ConvertSinecToDateTime(uint sinecTime)
    {
        // SINEC time starts from January 1, 1984
        DateTime baseDate = new DateTime(1984, 1, 1);

        // Convert seconds to TimeSpan
        TimeSpan timeSpan = TimeSpan.FromSeconds(sinecTime);

        // Add the TimeSpan to the base date
        DateTime realDateTime = baseDate.Add(timeSpan);

        return realDateTime;
    }
}
