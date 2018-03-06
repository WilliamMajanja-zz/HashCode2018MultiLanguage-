class Algorithm
  def self.perform(input)
    current_car_positions = []
    input[:cars].each do |car|
      current_car_positions << {x: 0, y: 0, can_move_at: 0}
    end

    current_time = 0
    while current_time <= input[:time]
      current_car_positions.each_with_index do |car, index|
        next if car[:can_move_at] > current_time
        best_ride_id = nil
        best_ride_weight = 0

        # FIND BEST RIDE
        input[:rides].each do |ride|
          next if ride[:assigned] 
          next if current_time > ride[:time][:finish]
          next if (ride[:time][:length] + current_time + distance(car[:x], car[:y], ride[:start_pos][:x], ride[:start_pos][:y])) > ride[:time][:finish]
          next if (ride[:time][:length] + current_time + distance(car[:x], car[:y], ride[:start_pos][:x], ride[:start_pos][:y])) > input[:time]
          worth = ride[:time][:length] + ((ride[:time][:start] - current_time) - distance(car[:x], car[:y], ride[:start_pos][:x], ride[:start_pos][:y])) >= 0 ? input[:ride_bonus] : 0
          if worth >= best_ride_weight
            best_ride_weight = worth
            best_ride_id = ride[:id]
          end
        end

        break if best_ride_id.nil?

        # SET YOUR STUFF
        input[:cars][index] << best_ride_id
        input[:rides][best_ride_id][:assigned] = true
        current_car_positions[index][:can_move_at] = current_time + distance(car[:x], car[:y], input[:rides][best_ride_id][:start_pos][:x], input[:rides][best_ride_id][:start_pos][:y]) + input[:rides][best_ride_id][:time][:length]
        current_car_positions[index][:x] = input[:rides][best_ride_id][:end_pos][:x]
        current_car_positions[index][:y] = input[:rides][best_ride_id][:end_pos][:y]
      end
      current_time +=1
    end

    return input
  end

  def self.distance(sx, sy, ex, ey)
    (sx - ex).abs + (sy - ey).abs
  end
end