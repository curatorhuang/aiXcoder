CREATE OR REPLACE FUNCTION CalculateTotalSales()
RETURNS NUMERIC AS $$
-- 函数说明：计算总销售额
DECLARE
    total_sales NUMERIC; -- 用于存储计算结果的变量
BEGIN
    -- 初始化变量
    total_sales := 0;
    -- 计算总销售额
    SELECT SUM(sales_amount) INTO total_sales
    FROM sales;
    -- 返回总销售额
    RETURN total_sales;

EXCEPTION
    WHEN OTHERS THEN
        -- 如果发生错误，则返回 NULL
        RETURN NULL;
END;
$$ LANGUAGE plpgsql;
