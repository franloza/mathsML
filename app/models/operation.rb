class Operation
  include Mongoid::Document
  field :firstOp, type: String
  field :secondOp, type: Integer
  field :responseTime, type: Numeric
  field :type, type: String
end
