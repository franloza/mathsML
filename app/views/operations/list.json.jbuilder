json.array!(@operations) do |operation|
  json.extract! operation, :id, :firstOp, :secondOp, :responseTime, :type
  json.url operation_url(operation, format: :json)
end
