class OperationsController < ApplicationController
  before_action :set_operation, only: [:show, :edit, :update, :destroy]

  # GET /operations
  # GET /operations.json
  def index

  end

  # GET /operations/list
  # GET /operations/list.json
  def list
    @operations = Operation.all
  end

  # GET /operations/1
  # GET /operations/1.json
  def show
  end

  # GET /operations/new
  def new
    @operation = Operation.new
    r = Random.new
    @operation.firstOp = r.rand(1...99)
    @operation.secondOp = r.rand(1...99)
    @operation.type = ['+','-','*','/'].sample
    @operation.initTime = Time.new
    @operation.save
  end

  # POST /operations
  # POST /operations.json
  def answer
    @operation = Operation.find(params[:id])
    
    if ((@operation.type == '+') && (operation_params.firstOp + operation_params.secondOp == params[:result]))
        @valid = true
    elsif ((@operation.type == '-') && (operation_params.firstOp - operation_params.secondOp == params[:result]))
        @valid = true
    elsif ((@operation.type == '*') && (operation_params.firstOp * operation_params.secondOp == params[:result]))
        @valid = true
    elsif  (@operation.type == '/') && (operation_params.firstOp / operation_params.secondOp == params[:result]))
        @valid = true
    else
      render :new
    end

    if (valid)
      @operation.endTime = Time.new
      @operation.save
      format.html { redirect_to @operation, notice: 'Operation was successfully created.' }
      format.json { render :show, status: :created, location: @operation }
    end
  end


  # GET /operations/1/edit
  def edit
  end

  # PATCH/PUT /operations/1
  # PATCH/PUT /operations/1.json
  def update
    respond_to do |format|
      if @operation.update(operation_params)
        format.html { redirect_to @operation, notice: 'Operation was successfully updated.' }
        format.json { render :show, status: :ok, location: @operation }
      else
        format.html { render :edit }
        format.json { render json: @operation.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /operations/1
  # DELETE /operations/1.json
  def destroy
    @operation.destroy
    respond_to do |format|
      format.html { redirect_to operations_url, notice: 'Operation was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_operation
      @operation = Operation.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def operation_params
      params.require(:operation).permit(:firstOp, :secondOp, :responseTime, :type)
    end
end
