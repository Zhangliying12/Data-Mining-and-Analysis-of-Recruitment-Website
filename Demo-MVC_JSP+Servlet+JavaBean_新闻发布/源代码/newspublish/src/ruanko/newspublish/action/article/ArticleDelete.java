package ruanko.newspublish.action.article;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import ruanko.newspublish.biz.ArticleBiz;


/**
 * 删除新闻
 * 
 * @author
 *
 */
public class ArticleDelete extends HttpServlet {
	private static final long serialVersionUID = -6612127874269742897L;

	/**
	 * 删新闻毕竟是一个危险操作，不能想删就删啊，所以用了post方式，给删除增加了一小点点难度
	 */
	@Override
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		//得到要删除id
		int id = Integer.parseInt(request.getParameter("id"));
		
		//创建业务逻辑对象，删除该新闻
		ArticleBiz articleBiz = new ArticleBiz ();
		articleBiz.delete(id);
		
		//跳转到主页
		//不过好像这里跳转到新闻列表页会更合适一些
		//也许这个问题会在下一版的《最小新闻发布系统》在解决吧
		request.getRequestDispatcher("index.jsp").forward(request, response);
		
	}
}
