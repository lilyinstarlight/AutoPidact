library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity AutoPidact is
	port(
		CLOCK_50_B5B : in    std_logic;
		GPIO         : inout std_logic_vector(35 downto 0)
	);
end entity AutoPidact;

architecture RTL of AutoPidact is
	signal spi_busy : std_logic;
	signal spi_rrdy  : std_logic;
	signal spi_rreq  : std_logic;
	signal spi_rdata : std_logic_vector(23 downto 0);

	signal mtr0_pwm : unsigned(6 downto 0);
	signal mtr0     : std_logic;
	signal mtr1_pwm : unsigned(6 downto 0);
	signal mtr1     : std_logic;
	signal mtr2_pwm : unsigned(6 downto 0);
	signal mtr2     : std_logic;
begin
	spi:  entity work.spi_slave
	      generic map(d_width => 24)
	      port map(sclk => GPIO(11), mosi => GPIO(12), miso => GPIO(13), ss_n => GPIO(14), busy => spi_busy, reset_n => '1', tx_load_en => '0', tx_load_data => "000000000000000000000000", rx_req => spi_rreq, rx_data => spi_rdata, trdy => open, rrdy => spi_rrdy, roe => open, st_load_en => '0', st_load_trdy => '0', st_load_rrdy => '0', st_load_roe => '0');

	spi_rreq <= spi_rrdy;

	mtr0_pwm <= unsigned(spi_rdata(6 downto 0));
	mtr1_pwm <= unsigned(spi_rdata(14 downto 8));
	mtr2_pwm <= unsigned(spi_rdata(22 downto 16));

	pwm0: entity work.PWM
	      generic map(cycle => 50000, width => 127)
	      port map(clk => CLOCK_50_B5B, pwm => to_unsigned(127, 7), q => mtr0);

	pwm1: entity work.PWM
	      generic map(cycle => 50000, width => 127)
	      port map(clk => CLOCK_50_B5B, pwm => to_unsigned(63, 7), q => mtr1);

	pwm2: entity work.PWM
	      generic map(cycle => 50000, width => 127)
	      port map(clk => CLOCK_50_B5B, pwm => to_unsigned(31, 7), q => mtr2);

	process(spi_rdata)
	begin
		if (spi_rdata(7) = '0') then
			GPIO(3) <= not(mtr0);
			GPIO(4) <= '1';
		else
			GPIO(3) <= '1';
			GPIO(4) <= not(mtr0);
		end if;

		if (spi_rdata(15) = '0') then
			GPIO(5) <= not(mtr1);
			GPIO(6) <= '1';
		else
			GPIO(5) <= '1';
			GPIO(6) <= not(mtr1);
		end if;

		if (spi_rdata(23) = '0') then
			GPIO(7) <= not(mtr2);
			GPIO(8) <= '1';
		else
			GPIO(7) <= '1';
			GPIO(8) <= not(mtr2);
		end if;
	end process;
end RTL;